# LangChain AI Assistant

This project is an AI-powered  assistant built using **LangChain**, **FastAPI**, and **Streamlit**. The chatbot interacts with users to answer questions using prompts and powerful AI models.

## Features

- **LangChain AI Agent**: A trading assistant powered by LangChain's AI capabilities.
- **Model Selection**: Predefined set of AI models such as "llama3-70b-8192" and "mixtral-8x7b-32768" are available for querying.
- **Customizable System Prompt**: Set a custom system prompt to guide the AI's responses based on the user's needs.
- **Simple Frontend**: The frontend is built with Streamlit for easy interaction with the AI agent.
![Screenshot 2025-01-20 at 01 08 17](https://github.com/user-attachments/assets/f51705c5-9550-4af3-b7fa-96fb9368a13d)

## Installation

### Prerequisites

- Python 3.7+
- Virtual environment (optional but recommended)

### Clone the repository

```bash
git clone https://github.com/poorvajasathasivam/llm-agent-chatbot.git
cd langchain-ai-trading-assistant
```
###  Create a virtual environment and activate it (optional):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

### Ensure you have the following environment variables set:

**Set up environment variables:**
Create a .env file in the root directory to store the environment variables. Example .env:

- GROQ_API_KEY = your_groq_api_key
- TAVILY_API_KEY = your_tavily_api_key
### Run the FastAPI Backend
To run the FastAPI app:

```bash
python app.py
``` 
The backend will be available at http://127.0.0.1:8000.

### Run the Streamlit Frontend
To run the Streamlit frontend:

```bash
streamlit run ui.py
``` 

The frontend will open at http://localhost:8501 by default.

### Usage
Set the system prompt: In the Streamlit frontend, define a system prompt to guide the AI on how to respond to queries. Example:

```bash
You are a financial trading assistant that can help users with trading strategies, market trends, and other financial concepts.
```

**Select a model:** Choose one of the available models like "llama3-70b-8192" or "mixtral-8x7b-32768."

**Enter a message:** Type a trading-related question or prompt in the message input box.

**Click "Submit"**: The FastAPI backend will process the input using LangChain and the selected AI model and return a response.

**Example Queries**
- "Can you explain what a moving average is and how it is used in stock trading?"
- "What is the difference between short and long positions in trading?"
- "Tell me about risk management in trading."




  
