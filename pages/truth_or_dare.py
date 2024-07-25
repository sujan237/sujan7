import streamlit as st
import random

# Define the Truth and Dare questions
truth_questions = [
    "What is the most embarrassing thing that has happened to you?",
    "Have you ever cheated in a game and not been caught?",
    "What is your biggest fear?",
    "What is the most childish thing you still do?",
    "What is the strangest dream you've ever had?",
    "If you could switch lives with someone for a day, who would it be and why?",
    "What is something you've never told anyone?",
    "What is your guilty pleasure?"
]

dare_tasks = [
    "Do your best impression of someone in the room and keep doing it until someone can guess who it is.",
    "Let the person to your left draw on your face with a pen.",
    "Sing everything you say for the next 10 minutes.",
    "Speak in an accent chosen by the group for the next 3 rounds.",
    "Do your best dance moves outside on the sidewalk.",
    "Eat a spoonful of a condiment chosen by the group.",
    "Let someone tickle you for 30 seconds."
]

# Function to randomly select a truth question
def get_truth_question():
    return random.choice(truth_questions)

# Function to randomly select a dare task
def get_dare_task():
    return random.choice(dare_tasks)

# Streamlit UI
st.title("Truth or Dare Game")

option = st.selectbox(
    "Choose Truth or Dare:",
    ("Truth", "Dare")
)

if option == "Truth":
    st.header("Truth Question:")
    st.write(get_truth_question())
elif option == "Dare":
    st.header("Dare Task:")
    st.write(get_dare_task())

st.markdown("---")

if st.button("New Truth or Dare"):
    st.empty()  # Clear previous output
