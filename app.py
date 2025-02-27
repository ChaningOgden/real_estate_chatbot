from preferences import save_preferences, load_preferences
from scraper import search_properties
from ml_model import train_neural_network, predict_next_properties

def chatbot():
    print("🤖 Welcome to your AI real estate assistant!")
    
    # Load preferences
    user_prefs = load_preferences()
    
    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye! Talk to you later.")
            break

        # Extract preferences and save
        preferences = {"location": "Chippewa Falls, WI", "price": 600000, "acres": 10}
        save_preferences(preferences)

        # Train or Load Model
        model = train_neural_network()
        
        # Predict properties
        suggested_properties = predict_next_properties(model, user_prefs)
        
        print("\n🏡 Recommended Properties:")
        for i, prop in enumerate(suggested_properties, 1):
            print(f"{i}. {prop['address']} - ${prop['price']} | {prop['acres']} acres")

        feedback = input("\nDid you like any of these? (yes/no): ").strip().lower()
        if feedback == "yes":
            liked_index = int(input("Which one? (1-3): ")) - 1
            save_preferences({"liked": suggested_properties[liked_index]})
        else:
            reason = input("What didn’t you like?: ").strip()
            save_preferences({"disliked_reason": reason})

if __name__ == "__main__":
    chatbot()