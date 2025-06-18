import streamlit as st

st.title("Chat Window")

with st.chat_message("assistant"):             # create chat message widget (explanation note ),eth ai assistance ane
    st.markdown("Hello, I am AI Assistant")     #markdown is a small type of markuplanguage like a html

with st.chat_message("human"):                   #create chat message widget into the user,human like a user
    st.markdown("I am planning vacation to Dubai")

message = st.chat_input("Enter your message")      #user nter cheyyanulla option,it is similar to the text_input

if message:
    with st.chat_message("human"):
        st.markdown(message)                      #st.write or markdown ubyogichu user type chytha content njmmuk write chyeyyendath

