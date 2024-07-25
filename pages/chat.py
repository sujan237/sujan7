import streamlit as st

# Dictionary to store information about Elon Musk
elon_info = {
    "biography": "Elon Musk is a business magnate, industrial designer, and engineer. He is the founder, CEO, CTO, and chief designer of SpaceX; early investor, CEO, and product architect of Tesla, Inc.; founder of The Boring Company; co-founder of Neuralink; and co-founder and initial co-chairman of OpenAI.",
    "tesla": "Tesla, Inc. is an American electric vehicle and clean energy company led by CEO Elon Musk. Tesla's products include electric cars, battery energy storage from home to grid-scale, solar panels and solar roof tiles, and related products and services.",
    "spacex": "SpaceX is an American aerospace manufacturer and space transport services company founded by Elon Musk. It is known for developing the Falcon launch vehicles and the Dragon spacecrafts, and is working towards the goal of enabling humans to live on other planets.",
    # Add more key-value pairs as needed for other queries
}

# Function to respond based on user input
def get_response(message):
    message_lower = message.lower()
    for key in elon_info:
        if key in message_lower:
            return elon_info[key]
    return "Sorry, I don't have information on that topic. Please ask about Elon Musk's biography, Tesla, or SpaceX."

# Streamlit app title
st.title("Elon Musk Chatbot")

# Display introductory message
st.markdown("Welcome to the Elon Musk chatbot! Ask me anything about Elon Musk.")

# Initialize an empty list to store chat history
chat_history = []

# Chat interface
user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        # Save user's message to chat history
        chat_history.append({"user": user_input, "type": "user"})
        
        # Get AI response based on user input
        ai_response = get_response(user_input)
        
        # Save AI's response to chat history
        chat_history.append({"user": ai_response, "type": "ai"})

# Display chat history
st.markdown("---")
for chat in chat_history:
    if chat["type"] == "user":
        st.text_input("You:", chat["user"], key=chat["user"])
    elif chat["type"] == "ai":
        st.text_input("Bot:", chat["user"], key=chat["user"])
