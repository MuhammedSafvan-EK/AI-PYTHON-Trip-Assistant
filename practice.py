#create ui application
import streamlit as st                  #import streamlit with the name of st
st.title("hello from upcode")           #title

name = st.text_input("enter your name:")#create textbox.user enter chyunna value variablekk store chyyan vendy name enna var create chythu

if st.button("SAY HELLO"):                  #create button (st - stramlit)
    st.write(f"hello {name},welcome to upcode")     #f-it represent python stringformat ,{name}-variable store chytha value hellok shehsam varum 