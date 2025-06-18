
# 🧙‍♂️ Dubai Trip Assistant – AI Travel Chatbot

Dubai Trip Assistant is an AI-powered chatbot that helps travelers plan their trip to Dubai. It provides intelligent recommendations for attractions, food spots, hotels, events, and generates personalized day-wise itineraries.

Built with Python, Streamlit, and OpenAI API, the app runs locally in your browser with a simple and interactive chat interface.

---

## 🚀 Features

- AI-based travel planning
- Chat interface with memory
- Suggestions for attractions, hotels, food, and events
- Personalized day-wise itinerary
- Runs locally via Streamlit

---

## 💻 Tech Stack

- Python 3.x  
- Streamlit  
- OpenAI API  
- `python-dotenv`  
- Git
 

✅ 1. Clone the Repository
git clone https://github.com/MuhammedSafvan-EK/AI-PYTHON-Trip-Assistant.git
cd dubai-trip-assistant


✅ 2. Create and Activate Virtual Environment
bash
Copy
Edit
python -m venv venv

 Windows
venv\Scripts\activate

 macOS/Linux
source venv/bin/activate


✅ 3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Or manually install:
bash
Copy
Edit
pip install streamlit openai python-dotenv


✅ 4. Add OpenAI API Key
Create a .env file in the project root:

env
Copy
Edit
OPENAI_API_KEY=your-openai-key-here
🔐 Never share your .env file publicly!


✅ 5. Run the App
bash
Copy
Edit
streamlit run app.py
Visit http://localhost:8501 in your browser.


## steps
1.create OpenAInAPI account
2.copy API_KEY to secure file
3.create .env- environment variable
4.store API key
5.ReferOpen AI Doc and Implement


### implementation plan
1.show messages
2.show textbox for input
3.once user input enter message,pass to openai
4.store response into message list and show in screen

🛡️ Security & Best Practices
Environment variables are stored in .env (ignored in .gitignore)

Never commit or push API keys or secrets

Use .env.example to guide collaborators

