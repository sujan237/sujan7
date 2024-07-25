import streamlit as st

# Dictionary to store information about Elon Musk
elon_info = {
    "biography": "Elon Musk is a business magnate, industrial designer, and engineer. He is the founder, CEO, CTO, and chief designer of SpaceX; early investor, CEO, and product architect of Tesla, Inc.; founder of The Boring Company; co-founder of Neuralink; and co-founder and initial co-chairman of OpenAI.",
    "tesla": "Tesla, Inc. is an American electric vehicle and clean energy company led by CEO Elon Musk. Tesla's products include electric cars, battery energy storage from home to grid-scale, solar panels and solar roof tiles, and related products and services.",
    "spacex": "SpaceX is an American aerospace manufacturer and space transport services company founded by Elon Musk. It is known for developing the Falcon launch vehicles and the Dragon spacecrafts, and is working towards the goal of enabling humans to live on other planets.",
    "neuralink": "Neuralink Corporation is a neurotechnology company founded by Elon Musk. It is developing implantable brain–machine interfaces, aiming to help people with neurological conditions and eventually achieve symbiosis with artificial intelligence.",
    "the boring company": "The Boring Company is an infrastructure and tunnel construction services company founded by Elon Musk. It aims to reduce traffic congestion in urban areas by creating a network of underground tunnels for electric vehicles.",
    "openai": "OpenAI is an artificial intelligence research laboratory and deployment company co-founded by Elon Musk. It aims to ensure that artificial general intelligence (AGI) benefits all of humanity.",
    "starship": "Starship is a fully reusable spacecraft being developed by SpaceX under the Starship and Super Heavy rocket system. It is designed to carry both crew and cargo on long-duration interplanetary flights.",
    "hyperloop": "Hyperloop is a proposed mode of passenger and freight transportation that would propel a pod-like vehicle through a near-vacuum tube at airline speeds. Elon Musk conceptualized the idea and SpaceX held a competition for pod designs.",
    "solarcity": "SolarCity was a solar energy services company founded by brothers Lyndon and Peter Rive. Elon Musk provided the initial concept and financial capital for SolarCity before its acquisition by Tesla, Inc. in 2016.",
    "paypal": "PayPal is an online payments system founded by Elon Musk, Peter Thiel, and Max Levchin. Musk was CEO and later sold it to eBay for $1.5 billion in 2002.",
    "zip2": "Zip2 Corporation was a city guide software for newspapers founded by Elon Musk and his brother Kimbal Musk. Compaq acquired Zip2 for $307 million in 1999.",
    "x.com": "X.com was an online payment company founded by Elon Musk in 1999, which later became PayPal after a merger.",
    "solar roof": "Tesla's Solar Roof is a solar energy product that integrates solar cells into roof tiles. It aims to combine solar energy generation with traditional roofing materials, offering an aesthetically pleasing and efficient solution.",
    "gigafactory": "Tesla's Gigafactory is a large-scale battery manufacturing facility in Nevada, USA. It produces battery cells and packs for Tesla electric vehicles and energy storage products.",
    "neural lace": "Neural lace is a hypothetical technology that integrates the human brain with AI, allowing for direct communication and augmentation of cognitive abilities. Elon Musk has expressed interest in developing this technology.",
    "dogecoin": "Elon Musk has shown interest and support for Dogecoin, a cryptocurrency featuring the Shiba Inu dog meme. His tweets and comments often influence its market value.",
    "mars colonization": "Elon Musk has expressed plans to colonize Mars as part of his vision for making humanity multiplanetary. SpaceX's Starship is intended to play a key role in this endeavor.",
    "ai safety": "Elon Musk is an advocate for artificial intelligence safety and regulation. He has warned about the potential dangers of AI and supports efforts to ensure it is developed responsibly.",
    "electric airplanes": "Elon Musk has discussed the possibility of developing electric airplanes as a means to reduce aviation's environmental impact.",
    "satellite internet": "SpaceX's Starlink project aims to provide global satellite internet coverage. Elon Musk envisions Starlink as a means to connect underserved and remote areas.",
    "cryptocurrency regulation": "Elon Musk has been vocal about the need for cryptocurrency regulation to prevent scams and ensure consumer protection.",
}

# Get a list of available topics from the elon_info dictionary
available_topics = list(elon_info.keys())

# Streamlit app title
st.title("Elon Musk Chatbot")

# Display introductory message
st.markdown("Welcome to the Elon Musk chatbot! Ask me anything about Elon Musk.")

# Initialize an empty list to store chat history
chat_history = []

# Function to respond based on user input
def get_response(message):
    message_lower = message.lower()
    for key in elon_info:
        if key in message_lower:
            return elon_info[key]
    return None

# Chat input widget
user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        # Save user's message to chat history
        chat_history.append({"user": user_input, "type": "user"})
        
        # Get AI response based on user input
        ai_response = get_response(user_input)
        
        if ai_response:
            # Save AI's response to chat history
            chat_history.append({"user": ai_response, "type": "ai"})
        else:
            # User asked about an unknown topic
            chat_history.append({"user": f"Sorry, I can only answer these questions: {', '.join(available_topics)}", "type": "ai"})

# Display chat history
st.markdown("---")
for chat in chat_history:
    if chat["type"] == "user":
        st.text_area("You:", chat["user"])
    elif chat["type"] == "ai":
        st.text_area("Bot:", chat["user"])
