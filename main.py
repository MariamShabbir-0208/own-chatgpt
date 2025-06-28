import os
from dotenv import load_dotenv
import chainlit as cl
from openai import AsyncClient  # Use AsyncClient from openai package
from typing import cast

# Load the environment variables from the .env file
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

@cl.on_chat_start
async def start():
    # Configure the OpenAI client for Gemini API
    external_client = AsyncClient(
        api_key=gemini_api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta",
    )

    # Initialize the agent configuration
    config = {
        "model": "gemini-1.5-flash",  # Use a valid Gemini model name
        "client": external_client,
        "tracing_disabled": True
    }

    # Set up the chat session
    cl.user_session.set("chat_history", [])
    cl.user_session.set("config", config)

    await cl.Message(content="Welcome to the Panaversity AI Assistant! How can I help you today?").send()

@cl.on_message
async def main(message: cl.Message):
    """Process incoming messages and generate responses."""
    # Send a thinking message
    msg = cl.Message(content="Thinking...")
    await msg.send()

    config = cast(dict, cl.user_session.get("config"))
    client = config["client"]
    model = config["model"]

    # Retrieve the chat history from the session
    history = cl.user_session.get("chat_history") or []
    
    # Append the user's message to the history
    history.append({"role": "user", "content": message.content})

    try:
        # Call the Gemini API using the OpenAI-compatible client
        response = await client.chat.completions.create(
            model=model,
            messages=history,
            temperature=0.7,
            max_tokens=1000
        )

        response_content = response.choices[0].message.content

        # Update the thinking message with the actual response
        msg.content = response_content
        await msg.update()

        # Append the assistant's response to the history
        history.append({"role": "assistant", "content": response_content})
        cl.user_session.set("chat_history", history)

        # Log the interaction
        print(f"User: {message.content}")
        print(f"Assistant: {response_content}")

    except Exception as e:
        msg.content = f"Error: {str(e)}"
        await msg.update()
        print(f"Error: {str(e)}")