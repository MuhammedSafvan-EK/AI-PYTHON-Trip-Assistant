
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
 
## steps

1.create OpenAInAPI account  <br>
2.copy API_KEY to secure file <br>
3.create .env- environment variable <br>
4.store API key <br>
5.ReferOpen AI Doc and Implement <br>


### implementation plan

1.show messages <br>
2.show textbox for input <br>
3.once user input enter message,pass to openai <br>
4.store response into message list and show in screen <br>


#### ✅ Run the App
streamlit run chatbot.py

🛡️ Security & Best Practices
Environment variables are stored in .env (ignored in .gitignore)

Never commit or push API keys or secrets

Use .env.example to guide collaborators

