from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import json
import time
import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv

# Load environment variables from a .env file for local development
load_dotenv()

# Initialize Firebase Admin SDK by loading the service account key from an environment variable.
# This is the recommended and most secure method for production environments.
try:
    firebase_admin.get_app()
except ValueError:
    try:
        # Get the JSON content from the environment variable
        credentials_json = os.environ.get("FIREBASE_CREDENTIALS_JSON")
        if credentials_json:
            # Load the credentials from the string
            cred = credentials.Certificate(json.loads(credentials_json))
            firebase_admin.initialize_app(cred)
    except Exception as e:
        print(f"Error initializing Firebase from environment variable or file: {e}")
        exit(1)

db = firestore.client()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# --- CONFIGURE GEMINI API ---
# The API key is now loaded from the environment
gemini_api_key = os.environ.get('GEMINI_API_KEY')
if not gemini_api_key:
    print("GEMINI_API_KEY not found in environment variables.")
    exit(1)

genai.configure(api_key=gemini_api_key)

# --- SASSY BOT PERSONALITY (FOR 'SPILL THE TEA' SECTION) ---
sassy_prompt = """
You are a sassy, gossip-loving best friend.
- Always respond with dramatic reactions, slang, and playful teasing.
- Use emojis and exaggerated tone.
- Always try to get MORE details about the gossip.
- Keep it light-hearted, never mean.
Example:
User: "I saw Alex with someone yesterday."
You: "OMG 😱 STOP IT. Was it who I think it was?? Details, NOW 👀"
"""

# --- GOSSIP REFINER PERSONALITY (FOR 'GET THE SCOOP' SECTION) ---
refiner_prompt = """
You are a witty, slightly mischievous gossip columnist.
- Take the provided piece of gossip and rephrase it to be more engaging and mysterious.
- Never make up new information, just rephrase the existing gossip.
- Use phrases like "Whispers are..." or "The buzz around town is..."
- Keep it short, intriguing, and a little playful.
Example:
Gossip: "I heard Alex got a new job."
You: "The buzz is that Alex landed a new gig, and it's a juicy one!"
"""

# --- HELPER FUNCTION TO SAVE GOSSIP TO FIRESTORE ---
def save_gossip_to_db(gossip_text):
    doc_ref = db.collection("gossip_items").document()
    doc_ref.set({
        "text": gossip_text,
        "timestamp": firestore.SERVER_TIMESTAMP
    })

# --- ROUTE FOR SPILL THE TEA (GOSSIP COLLECTOR) ---
@app.route("/spill_tea", methods=["POST"])
def spill_tea():
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    # Save the user's message to the database
    save_gossip_to_db(user_message)
    
    # Exponential backoff for API calls
    retries = 0
    while retries < 5:
        try:
            response = genai.GenerativeModel("gemini-1.5-flash").generate_content(
                sassy_prompt + "\nUser: " + user_message
            )
            return jsonify({"reply": response.text})
        except Exception as e:
            print(f"API call failed, retrying in {2**retries} seconds... Error: {e}")
            time.sleep(2**retries)
            retries += 1
    
    return jsonify({"error": "Failed to get response from Gemini API after multiple retries"}), 500


# --- HELPER FUNCTION TO GET GOSSIP FROM FIRESTORE ---
def get_unread_gossip(user_id):
    # Get all gossip items in a single pass
    gossip_documents = list(db.collection("gossip_items").stream())
    
    # Get the user's seen gossip IDs
    seen_gossip_ids = [doc.id for doc in db.collection(f"users/{user_id}/seen_gossip").stream()]

    # Find an unread gossip item
    for doc in gossip_documents:
        if doc.id not in seen_gossip_ids:
            # We found an unread item, return its ID and content
            return doc.id, doc.to_dict()
    
    # If no unread gossip is found, return None
    return None, None


# --- ROUTE FOR GET THE SCOOP (GOSSIP PROVIDER) ---
@app.route("/get_scoop", methods=["POST"])
def get_scoop():
    data = request.json
    user_id = data.get("user_id", "anonymous_user") # Assuming a user_id is sent from the frontend

    # Try to get an unread gossip item
    unread_id, unread_gossip = get_unread_gossip(user_id)

    if unread_gossip:
        # Use a separate Gemini model to refine the gossip
        retries = 0
        while retries < 5:
            try:
                # Pass the raw gossip to the refiner prompt to generate a witty reply
                response = genai.GenerativeModel("gemini-1.5-flash").generate_content(
                    refiner_prompt + "\nGossip: " + unread_gossip["text"]
                )
                
                sassy_reply = response.text
                
                # Mark the gossip as seen by the user
                db.collection(f"users/{user_id}/seen_gossip").document(unread_id).set({})
                return jsonify({"reply": sassy_reply})
            except Exception as e:
                print(f"API call to get scoop failed, retrying in {2**retries} seconds... Error: {e}")
                time.sleep(2**retries)
                retries += 1
        
        # If all retries fail, return a default error message
        return jsonify({"error": "Failed to get scoop after multiple retries"}), 500
    else:
        return jsonify({"reply": "I'm all out of tea! Spill some more for me to share."})

if __name__ == "__main__":
    app.run(debug=True)
