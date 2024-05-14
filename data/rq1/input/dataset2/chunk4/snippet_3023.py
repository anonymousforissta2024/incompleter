#Source: https://stackoverflow.com/questions/76026817/unable-to-resolve-the-error-typeerror-nonetype-object-is-not-subscriptable-w
import os
import nltk
import ssl
import streamlit as st
import random
import fastf1 as ff1
import pandas as pd
st.title("F1bot")
st.write("Welcome to the F1bot. Please type a message and press Enter to ask questions related to F1.")
counter=0
counter += 1
st.write('Enter the year')
year=st.number_input("You:", key=f"user_input_{counter}")
counter+=1
st.write('Enter the venue')
venue=st.text_input("You:", key=f"user_input_{counter}")
counter+=1
st.write('Enter the race type whether it is quali or final')
rtype=st.text_input("You:", key=f"user_input_{counter}")
if rtype=='quali':
    rtype='Q'
elif rtype=='final':
    rtype='R'
quali = ff1.get_session(year,venue,rtype)
st.write("Chatbot:", value=quali.event, height=100, max_chars=None, key=f"chatbot_response_{counter}")
st.write("Thank you for chatting with me. Have a great day!")
st.stop()