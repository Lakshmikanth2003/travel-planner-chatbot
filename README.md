# Travel Planner Chatbot

An interactive chatbot designed to help users plan their trips by providing information about places to visit, restaurants, famous foods, and hotels in various destinations.

## Description

The **Travel Planner Chatbot** helps users find information for planning their trips. It provides:

- **Places to visit**: Information on tourist spots and key attractions in various destinations.
- **Restaurants**: A list of recommended restaurants based on cuisine, price range, and description.
- **Famous foods**: Local delicacies and must-try dishes.
- **Hotels**: Hotel recommendations with ratings, price ranges, and descriptions.

The chatbot allows users to interactively ask questions about these topics for any destination they wish to visit.

## Requirements

- **Python 3.x**: Ensure you have Python version 3.x installed. You can download it from [here](https://www.python.org/downloads/).
- **No additional libraries**: This project uses only built-in Python libraries like `json` and `os`.

## Installation

To set up the project on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/<your-username>/travel-planner-chatbot.git

2. Navigate into the project directory: cd travel-planner-chatbot

3.Run the chatbot: python chatbot.py




"HOW TO USE":
1.After starting the chatbot, you will be prompted to enter a destination (e.g., "Goa").
2.Once you provide a destination, the chatbot will ask what category you would like to know about:
*Places to visit
*Restaurants
*Famous foods
*Hotels
3.Based on your choice, the chatbot will display relevant information for the selected destination.
4.You can ask multiple questions or change the category as needed during the conversation.





Design Choices:
1.Data Storage: The destination data (places, restaurants, foods, hotels) is stored within the Python code in a dictionary format. This approach is simple for a small-scale project. For larger projects, consider using a database or external API for dynamic data retrieval.

2.Dialogue Management: The chatbot tracks the user's preferences, such as the destination and category. This makes the conversation flow more naturally, remembering the previous inputs to avoid re-entering data.

3.Error Handling: Basic error handling is implemented for missing or incorrect data, and the chatbot asks for clarification when necessary.


Challenges:
1.Handling ambiguous or unclear user inputs was one of the challenges. Basic clarification mechanisms have been implemented, but there's potential for more advanced features.

2.Implementing a user-friendly conversational flow took time, especially ensuring that the chatbot remembers past choices and provides useful information without overwhelming the user.



Potential Improvements:
1.API Integration: Fetch live data from external APIs (e.g., hotel booking services, real-time restaurant reviews).

2.Natural Language Processing (NLP): Implement NLP to handle more complex user inputs and allow more flexibility in conversation.

3.More Destinations: Add data for more destinations and expand the chatbot's knowledge.

4.User Interface: Integrate the chatbot into a graphical user interface (GUI) or web application for an improved user experience.


