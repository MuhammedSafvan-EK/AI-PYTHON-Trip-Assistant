from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st
                 
load_dotenv()                         

client = OpenAI()



initial_message = [
     {"role": "system", "content": "You are a trip planner in Dubai.You are an expert in Dubai Tourism, locations, food, events, hotels, etc. You are able to guide users to plan the vacations to Dubai. You should respond professionally. your name is Dubai Genie, short name DG.  response shouldn't exceed be 200  words. Always ask questions to user and help them to plan the trip. Finally give a day Wise itinerary. Deal with user professionally."},      
        {
            "role": "assistant",                                                     
            "content": "Hello, I am Dubai Genie, your expert trip planner. How can I help you."  
        }
]

#function to get resoponse from Open AI LLM
def get_response_from_llm(messages):                    
    completion = client.chat.completions.create(                               
        model="gpt-4o-mini",                                                    
        messages=messages                                                             
    )
    return completion.choices[0].message.content                       
# ----------------------------------------------------------

#intialize with intial message
if "messages" not in st.session_state:
    st.session_state.messages = initial_message 

st.title("🏙️Dubai Trip Assistant App")


#--display previous chat content in ui
for message in st.session_state.messages:           
    if message["role"] != "system":
       with st.chat_message(message["role"]):          
            st.markdown(message["content"])


user_message = st.chat_input("Enter your message")          
if user_message:                                            
    new_message = {
            "role": "user",                                                      
            "content": user_message 
        }                                                      
    st.session_state.messages.append(new_message)                          
    with st.chat_message(new_message["role"]):
        st.markdown(new_message["content"])

        
    response = get_response_from_llm( st.session_state.messages)            
    if response:                           
        response_message = {
            "role": "assistant",                                                      
            "content": response
        }   
        st.session_state.messages.append(response_message)                   
        with st.chat_message(response_message["role"]):
           st.markdown(response_message["content"])          