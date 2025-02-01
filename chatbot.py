import json

# Load destination data from JSON file
def load_data():
    with open("data/destinations.json", "r", encoding="utf-8") as file:
        return json.load(file)

# Function to get information based on user query
def get_info(destination, category):
    data = load_data()  # Load data from JSON file
    destination = destination.title()  # Capitalize first letter of each word

    if destination in data:
        category_data = data[destination].get(category, None)
        
        if category_data:
            response = "\nHere is what I found:"
            for item in category_data:
                response += f"\n\n- **{item['name']}**"
                response += f"\n   Description: {item['description']}"
            return response  # This returns the formatted response

        else:
            return f"Sorry, I don't have any information for {category} in {destination}."
    else:
        return f"Sorry, I don't have information for {destination}."


# Main chatbot loop
def chatbot():
    print("Welcome to the Travel Planner Chatbot! (Type 'exit' to stop)")
    
    while True:
        user_input = input("\nWhere do you want to travel? ").strip().lower()
        if user_input == "exit":
            print("Goodbye! Safe travels! ✈️")
            break

        print("\nWhat would you like to know? Options: places_to_visit, restaurants, famous_foods, hotels")
        category = input("Enter category: ").strip().lower()

        # Fetch information
        response = get_info(user_input, category)

        # Print response
        if isinstance(response, list) and response:
            print("\nHere is what I found:")
            for item in response:
                print(f"- {item['name']}: {item['description']}")
        else:
            print(response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()
