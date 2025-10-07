import streamlit as st
import spacy

# --- Setup and Loading ---
# Load the spaCy model once
@st.cache_resource
def load_spacy_model():
    return spacy.load("en_core_web_sm")

nlp = load_spacy_model()

# --- The Chatbot's Knowledge Base ---
knowledge_base = {
    "Definition of Mangroves":
        "A mangrove forest is a unique and vital ecosystem found along coastal intertidal zones. They are forests of salt-tolerant trees that thrive in muddy, oxygen-poor soil.",
    
    "Flora and Plants":
        "The flora is highly specialized. Key species include:\n"
        "   - **Red Mangroves:** Known for their tangled, reddish prop roots.\n"
        "   - **Black Mangroves:** Have special roots (pneumatophores) that stick up from the soil to get oxygen.\n"
        "   - **White Mangroves:** Typically grow at higher elevations.",

    "Fauna and Wildlife":
        "Mangrove forests are bursting with animal life! 🦀 They are a critical habitat for crustaceans (like crabs and shrimp), many species of fish, birds (like herons and kingfishers), and even some mammals like monkeys or the Royal Bengal Tiger!",

    "Economic Importance":
        "Mangrove forests have significant economic importance: 💰\n"
        "   - **Fisheries:** They are breeding grounds for fish and shellfish.\n"
        "   - **Timber & Fuel:** The wood is valuable for building.\n"
        "   - **Coastal Protection:** They act as natural barriers, saving billions in storm damage.",

    "Tourism in Mangroves":
        "Ecotourism in mangrove forests is growing. 🏞️ Activities include boat tours, kayaking, bird watching, and educational walks on boardwalks.",

    "Ecological Benefits":
        "The ecological benefits of mangroves are immense: 🌍\n"
        "   - **Coastal Defense:** They prevent erosion.\n"
        "   - **Carbon Storage:** They are incredibly efficient at capturing carbon dioxide (Blue Carbon).\n"
        "   - **Water Filtration:** They trap pollutants, cleaning the water.",
}

help_response = (
    "I can answer questions about the following topics. You can ask a question or click a button below:\n\n"
    "   - **Definition:** What they are.\n"
    "   - **Flora:** The types of plants and trees.\n"
    "   - **Fauna:** The kinds of animals and wildlife.\n"
    "   - **Economic Importance:** Their value to humans.\n"
    "   - **Tourism:** Visiting and activities.\n"
    "   - **Ecological Benefits:** Their role in the environment."
)
knowledge_base["Help"] = help_response

def get_bot_response(user_query):
    """
    Finds the best response using spaCy's semantic similarity.
    """
    # Process the user's query with spaCy
    query_doc = nlp(user_query.lower())
    
    # Handle direct commands first
    if "help" in user_query.lower():
        return knowledge_base["Help"], "Help"
        
    best_score = 0
    best_match_topic = None

    # Compare the user query to each topic in the knowledge base
    for topic, content in knowledge_base.items():
        topic_doc = nlp(topic.lower())
        score = query_doc.similarity(topic_doc)
        
        if score > best_score:
            best_score = score
            best_match_topic = topic

    # Set a confidence threshold for the similarity score
    if best_score >= 0.70:
        # Store the current topic for conversation context (memory)
        st.session_state.current_topic = best_match_topic
        return knowledge_base[best_match_topic], best_match_topic
    else:
        # If no confident match, check for follow-up questions
        if "current_topic" in st.session_state and st.session_state.current_topic:
            # A simple context check (this could be made more advanced)
            if any(word in user_query.lower() for word in ["they", "it", "more", "tell me more"]):
                 return knowledge_base[st.session_state.current_topic], st.session_state.current_topic

        st.session_state.current_topic = None
        return "I'm sorry, my knowledge is strictly about Mangrove Forests. Could you please ask a question about one of the topics? You can type 'help' to see them.", None


# --- Streamlit GUI ---
st.set_page_config(page_title="Advanced Chatter Box", layout="wide")
st.title("🌿 Advanced Chatter Box: Your Mangrove Forest Guide")

# Initialize chat history and context
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.current_topic = None

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Suggested Topic Buttons ---
st.sidebar.title("Topics")
st.sidebar.markdown("Click a topic to learn more!")
for topic in knowledge_base.keys():
    if st.sidebar.button(topic):
        response, matched_topic = get_bot_response(topic)
        st.session_state.messages.append({"role": "user", "content": f"Tell me about: **{topic}**"})
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun() # Rerun the app to display the new messages

# --- Chat Input and Logic ---
if prompt := st.chat_input("Ask a question or type 'help'..."):
    # User message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Bot response
    response, matched_topic = get_bot_response(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})