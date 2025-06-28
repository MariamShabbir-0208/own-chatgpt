Own ChatGPT
A custom chatbot application built using the Gemini API and Chainlit, designed to provide an interactive conversational experience similar to ChatGPT. This project allows users to interact with a web-based chatbot powered by Google's generative AI, with a simple and intuitive interface.
Features

Interactive Chat Interface: Built with Chainlit for a user-friendly web-based chat experience.
Gemini API Integration: Uses Google's Gemini API for generating responses.
Chat History: Maintains conversation history for contextual responses.
Error Handling: Robust error handling for API calls and user interactions.

Prerequisites

Python 3.12 or higher
A valid Gemini API key from Google Cloud Console
Poetry or pip for dependency management

Installation

Clone the Repository:
git clone <repository-url>
cd own-chatgpt


Set Up Environment Variables:

Create a .env file in the project root.
Add your Gemini API key:GEMINI_API_KEY=your-api-key-here




Install Dependencies:

If using Poetry:poetry install


If using pip:pip install chainlit openai python-dotenv





Dependencies
The project requires the following Python packages (specified in pyproject.toml):

chainlit>=2.5.5: For the web-based chat interface.
openai>=1.93.0: For interacting with the Gemini API using OpenAI-compatible client.
python-dotenv>=1.1.1: For loading environment variables.

Usage

Run the Application:
chainlit run app.py

This starts the Chainlit server, typically accessible at http://localhost:8000.

Interact with the Chatbot:

Open your browser and navigate to http://localhost:8000.
Type a message (e.g., "Hello, how are you?") to start a conversation.
The chatbot will respond using the Gemini API, and the conversation history is maintained for context.



Project Structure

app.py: Main application file containing the chatbot logic.
.env: Environment file for storing the Gemini API key.
pyproject.toml: Project configuration and dependencies.

Configuration

Gemini API Key: Ensure the GEMINI_API_KEY is set in the .env file.
Model: The default model is gemini-1.5-flash. Update the model name in app.py if needed (refer to Gemini API documentation for available models).
API Endpoint: The base URL is set to https://generativelanguage.googleapis.com/v1beta. Verify compatibility with the Gemini API documentation.

Troubleshooting

API Key Errors: Ensure your Gemini API key is valid and the API is enabled in Google Cloud Console.
Dependency Issues: Verify all dependencies are installed correctly using Poetry or pip.
Connection Issues: Check your internet connection and the Gemini API endpoint status.
If you encounter errors, check the console logs for details and ensure the model name and API key are correct.

Contributing
Contributions are welcome! Please submit a pull request or open an issue for suggestions or bug reports.
License
This project is licensed under the MIT License.