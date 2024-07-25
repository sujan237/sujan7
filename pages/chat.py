import streamlit as st
from datetime import datetime

# Title of the chat app
st.title("Simple Chat App")

# Initialize an empty dictionary to store messages
messages = {}

# Function to display messages
def display_messages(messages):
    for message_time, message_text in messages.items():
        st.write(f"[{message_time}] User: {message_text}")

# Input box for user to send messages
user_input = st.text_input("Send a message:")

# Button to send the message
if st.button("Send"):
    if user_input:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        messages[current_time] = user_input
        st.success("Message sent!")

# Display all messages
st.header("Chat History")
display_messages(messages)
