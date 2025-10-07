import streamlit as st
from fuzzywuzzy import process

# --- The Chatbot's Knowledge Base ---
# Keys are the canonical questions/topics. The bot will match user input to these.
knowledge_base = {
    "What are mangrove forests?":
        "A mangrove forest is a unique and vital ecosystem found along coastal intertidal zones. They are forests of salt-tolerant trees that thrive in muddy, oxygen-poor soil.",
    
    "What is the flora, plants, or trees in mangroves?":
        "The flora is highly specialized. Key species include:\n"
        "   - **Red Mangroves:** Known for their tangled, reddish prop roots.\n"
        "   - **Black Mangroves:** Have special roots (pneumatophores) that stick up from the soil to get oxygen.\n"
        "   - **White Mangroves:** Typically grow at higher elevations.",

    "What is the fauna, animals, or wildlife in mangroves?":
        "Mangrove forests are bursting with animal life! 🦀 They are a critical habitat for:\n"
        "   - **Crustaceans:** Fiddler crabs, mud lobsters, and shrimp.\n"
        "   - **Fish:** Mangrove roots act as a nursery for many species of fish.\n"
        "   - **Birds:** Herons, egrets, and kingfishers use mangroves for nesting and feeding.\n"
        "   - **Mammals:** Some are even home to monkeys, otters, and the Royal Bengal Tiger!",

    "What is the economic importance or value of mangroves?":
        "Mangrove forests have significant economic importance: 💰\n"
        "   - **Fisheries:** They are breeding grounds for fish and shellfish, supporting commercial fishing.\n"
        "   - **Timber & Fuel:** The wood is valuable for building and charcoal.\n"
        "   - **Coastal Protection:** They act as natural barriers, saving billions in infrastructure damage from storms.",

    "What about tourism in mangrove forests?":
        "Ecotourism in mangrove forests is growing. 🏞️ Activities include:\n"
        "   - **Boat Tours & Kayaking** to explore the unique waterways.\n"
        "   - **Bird Watching** for rare and beautiful species.\n"
        "   - **Boardwalks & Nature Trails** for educational walks.",

    "What are the ecological benefits of mangroves?":
        "The ecological benefits of mangroves are immense: 🌍\n"
        "   - **Coastal Defense:** They absorb the impact of waves and prevent erosion.\n"
        "   - **Carbon Storage:** They are incredibly efficient at capturing carbon dioxide (Blue Carbon).\n"
        "   - **Water Filtration:** They trap pollutants, cleaning the water that flows into the ocean.",
}

# --- Help Command Response ---
# Placed here for easy access
help_response = (
    "I can answer questions about the following topics related to Mangrove Forests:\n\n"
    "   - **Definition:** What they are.\n"
    "   - **Flora:** The types of plants and trees.\n"
    "   - **Fauna:** The kinds of animals and wildlife.\n"
    "   - **Economic Importance:** Their value to humans.\n"
    "   - **Tourism:** Visiting and activities.\n"
    "   - **Ecological Benefits:** Their role in the environment.\n\n"
    "Just type your question in the box below!"
)
knowledge_base["help"] = help_response


def get_best_match(user_query, choices):
    """
    Finds the best match for the user's query from a list of choices.
    Uses fuzzywuzzy's process.extractOne to find the best match and its similarity score.
    """
    best_match = process.extractOne(user_query, choices)
    return best_match

# --- Streamlit GUI ---

st.title("🌿 Chatter Box: Your Mangrove Forest Guide")
st.markdown("Ask me anything about mangrove forests, or type **'help'** to see a list of topics.")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What would you like to know?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # --- Bot Logic ---
    # Find the best matching question from the knowledge base
    questions = list(knowledge_base.keys())
    match, score = get_best_match(prompt.lower(), questions)

    # Set a confidence threshold
    if score >= 75:
        response = knowledge_base[match]
    else:
        response = "I'm sorry, my knowledge is strictly about Mangrove Forests. Could you please ask a question about one of the topics listed in the 'help' command?"
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})