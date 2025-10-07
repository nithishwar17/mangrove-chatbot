# PROJECT 4: CHATTER BOX - Mangrove Forest Guide

def chatbot():
    """
    A simple rule-based chatbot that provides information about Mangrove Forests.
    """
    
    # --- The complete Knowledge Base ---
    knowledge_base = {
        ('hello', 'hi', 'hey', 'greetings'): 
            "Hello! I am Chatter Box, your expert guide to Mangrove Forests. 🌿\n"
            "You can ask me about their flora, fauna, economic importance, tourism, and ecological benefits. "
            "Type 'quit' or 'exit' to end our chat.",

        ('mangrove', 'what is a mangrove', 'define mangrove'):
            "A mangrove forest is a unique and vital ecosystem found along coastal intertidal zones in tropical and subtropical regions. "
            "They are forests of salt-tolerant trees that thrive in muddy, oxygen-poor soil.",

        ('flora', 'plants', 'trees', 'vegetation'):
            "The flora of mangrove forests is highly specialized. Key species include:\n"
            "   - **Red Mangroves:** Known for their tangled, reddish prop roots.\n"
            "   - **Black Mangroves:** Have special roots called pneumatophores that stick up from the soil to get oxygen.\n"
            "   - **White Mangroves:** Typically grow at higher elevations.",

        ('fauna', 'animals', 'wildlife', 'creatures'):
            "Mangrove forests are bursting with animal life! 🦀 They are a critical habitat for:\n"
            "   - **Crustaceans:** Fiddler crabs, mud lobsters, and shrimp.\n"
            "   - **Fish:** Mangrove roots act as a nursery for many species of fish.\n"
            "   - **Birds:** Herons, egrets, and kingfishers use mangroves for nesting and feeding.\n"
            "   - **Mammals:** Some are even home to monkeys, otters, and the Royal Bengal Tiger!",

        ('economic', 'economy', 'importance', 'value', 'money'):
            "Mangrove forests have significant economic importance: 💰\n"
            "   - **Fisheries:** They are breeding grounds for fish and shellfish, supporting commercial fishing.\n"
            "   - **Timber & Fuel:** The wood is valuable for building and charcoal.\n"
            "   - **Coastal Protection:** They act as natural barriers, saving billions in infrastructure damage from storms.",

        ('tourism', 'tourist', 'visit', 'travel'):
            "Tourism in mangrove forests is a growing form of ecotourism. 🏞️ Activities include:\n"
            "   - **Boat Tours & Kayaking** to explore the unique waterways.\n"
            "   - **Bird Watching** for rare and beautiful species.\n"
            "   - **Boardwalks & Nature Trails** for educational walks.",

        ('ecological', 'benefits', 'environment', 'ecosystem'):
            "The ecological benefits of mangroves are immense: 🌍\n"
            "   - **Coastal Defense:** They absorb the impact of waves and prevent erosion.\n"
            "   - **Carbon Storage:** They are incredibly efficient at capturing carbon dioxide, helping fight climate change.\n"
            "   - **Water Filtration:** They trap pollutants, cleaning the water.",
        
        ('help', 'topics', 'what can you do'):
             "I can tell you about the following topics related to Mangrove Forests:\n"
             "- What a mangrove is\n"
             "- Flora (plants)\n"
             "- Fauna (animals)\n"
             "- Economic importance\n"
             "- Tourism\n"
             "- Ecological benefits"
    }

    print("Hello! I am Chatter Box, your expert guide to Mangrove Forests. 🌿")
    print("Type 'quit' or 'exit' to end our chat.")
    print("-" * 70)

    while True:
        user_input = input("You: ").lower().strip()

        # Check for exit command FIRST.
        if user_input in ("quit", "exit", "bye", "goodbye"):
            print("Chatter Box: Thank you for chatting! Have a great day.")
            break

        found_response = False
        for keywords, response in knowledge_base.items():
            if any(keyword in user_input for keyword in keywords):
                print("Chatter Box:", response)
                found_response = True
                break
        
        # This is the final, polite refusal for off-topic questions.
        if not found_response:
            print("Chatter Box: I'm sorry, my knowledge is strictly about Mangrove Forests. "
                  "Could you please ask a question about their flora, fauna, economic importance, tourism, or ecological benefits?")

# This part stays the same
if __name__ == "__main__":
    chatbot()