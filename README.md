<img width="3188" height="1202" alt="frame (3)" src="https://github.com/user-attachments/assets/517ad8e9-ad22-457d-9538-a9e62d137cd7" />


# gossip central 🎯


## Basic Details
### Team Name: bit by bit


### Team Members
- Team Lead: lena  - CUSAT
- Member 2: MALAVIKA - CUSAT
- Member 3: [Name] - [College]

### Project Description
This project is a playful, interactive system where gossip collected from users on one dashboard is delivered to users on the other dashboard through an AI-powered chatbot. The idea is to simulate a “gossip pipeline” between two separate communities, with the chatbot acting as both a listener and a storyteller.

### The Problem (that doesn't exist)
Do you need a ridiculuos motivation to go to college well we hav that set up for you

### The Solution (that nobody asked for)
Your gossip friend that gives you the latest and ongoing gossip and also if you do want to add fuel you have the chance to

## Technical Details
### Technologies/Components Used
For Software:
- python
- flask
- firebase
- [Tools used]

For Hardware:
- [List main components]
- [List specifications]
- [List tools required]

### Implementation
For Software:
# Installation
[commands]

# Run
[commands]

### Project Documentation
For Software:Project Report: The Gossip App
1. Executive Summary
The Gossip App is a full-stack web application designed to facilitate anonymous, AI-driven gossip sharing and retrieval. The system is comprised of a Flask-based backend and a JavaScript/HTML frontend. The core innovation lies in the use of the Gemini API to power two distinct chatbot personalities: a "sassy" bot for receiving gossip and a "relatable" bot for delivering it. This report outlines the application's design, functionality, and technical implementation.

2. Introduction
The objective of the Gossip App is to create an engaging and interactive platform for users to anonymously share and consume light-hearted gossip. The application provides a simple, intuitive user interface that abstracts away the complexity of the underlying API calls. It serves as a proof-of-concept for how different AI personalities can be integrated to create varied user experiences within a single application.

3. Technical Architecture
The application employs a client-server architecture.

Frontend
The frontend is a single index.html file that contains all necessary HTML, CSS, and JavaScript. It is responsible for:

Displaying the main landing page.

Managing the two modal chat windows.

Handling user input and dynamically adding messages to the chat logs.

Making fetch requests to the backend endpoints for "Spill the Tea" and "Get the Scoop" functionality.

Backend
The backend is a Flask application (app.py) that acts as the central hub for the application. Its responsibilities include:

Serving the index.html file.

Defining and managing the API endpoints.

Interfacing with the Google Gemini API using two predefined prompts to generate conversational responses.

(Note: The current implementation uses an in-memory list (gossip_log) for storing gossip. A production-ready version would replace this with a persistent database like Firebase Firestore, as mentioned in the project documentation.)

4. Core Functionality
The application offers two primary user interactions, each managed by a dedicated chatbot personality.

Spill the Tea
This function allows a user to submit an anonymous gossip item.

User Interaction: The user types a message into the "Spill the Tea" modal.

Backend Process: The message is sent to the /spill_tea endpoint. The backend uses the "sassy" Gemini personality prompt to generate a dramatic and engaging response, which is returned to the user.

Data Storage: The user's original message is stored in the gossip_log for later retrieval.

Get the Scoop
This function retrieves and presents a stored gossip item to the user.

User Interaction: The user types a message to initiate the conversation in the "Get the Scoop" modal.

Backend Process: The backend retrieves a gossip item from the gossip_log. It then uses the "relatable" Gemini personality prompt to rephrase the gossip in a curious and friendly tone, returning the new message to the user.

Data Management: The current implementation uses the in-memory gossip_log. For a persistent solution, the backend would manage marking gossip as "read" to prevent repetition.

5. API Reference
The Flask backend provides two primary API endpoints for handling user interactions.

POST /spill_tea
Description: Submits a user's gossip and receives a sassy AI response.

Request Body: {"message": "string"}

Response Body: {"reply": "string"}

POST /get_scoop
Description: Retrieves a gossip item and receives a relatable AI response.

Request Body: {"message": "string"}

Response Body: {"reply": "string"}

6. Conclusion
The Gossip App successfully demonstrates the integration of a full-stack web application with the Gemini API to create a dynamic, personality-driven user experience. The modular design, with clear separation of frontend and backend concerns, provides a solid foundation for future enhancements, such as database integration and user authentication.

# Screenshots (Add at least 3)



![WhatsApp Image 2025-08-09 at 17 41 51_7ce01f2c](https://github.com/user-attachments/assets/64832b22-5bc5-4949-8b2e-5bdc47c7afc3)
homepage






![WhatsApp Image 2025-08-09 at 17 45 53_a62c6807](https://github.com/user-attachments/assets/42517192-983c-4b40-97bc-7c04691c9efc)
chatbot of gossip taker


![WhatsApp Image 2025-08-09 at 17 47 44_2dcce789](https://github.com/user-attachments/assets/e0c89f21-ee4d-4b04-a5f8-a3ac027bfff4)

chatbot of gossip giver

# Diagrams
![Workflow](Add your workflow/architecture diagram here)
*Add caption explaining your workflow*

For Hardware:

# Schematic & Circuit
![Circuit](Add your circuit diagram here)
*Add caption explaining connections*

![Schematic](Add your schematic diagram here)
*Add caption explaining the schematic*

# Build Photos
![Components](Add photo of your components here)
*List out all components shown*

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

### Project Demo
# Video
[Add your demo video link here]
*Explain what the video demonstrates*

# Additional Demos
[Add any extra demo materials/links]

## Team Contributions
Lena-made first chatbot
Malavika-Made second chatbpt

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--25-25?link=https%3A%2F%2Fwww.tinkerhub.org%2Fevents%2FQ2Q1TQKX6Q%2FUseless%2520Projects)
