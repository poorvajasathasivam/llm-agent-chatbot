from fastapi import FastAPI
from pydantic import BaseModel
from typing import List 
from langchain_community.tools.tavily_search import TavilySearchResults
import os 
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# Get all the API KEYS 
groq_api_key = os.getenv('GROQ_API_KEY')
tavily_api_key = os.getenv('TAVILY_API_KEY')

# Predefined set of models 
MODEL_NAMES = [
    "llama3-70b-8192",
    "mixtral-8x7b-32768"
]

tool_tavily = TavilySearchResults(max_results=2)

tools = [tool_tavily,]

app = FastAPI(title="LangGraph AI Agent")

class RequestState(BaseModel):
    model_name: str
    system_prompt: str
    messages: List[str]
    
    
# Defining an endpoint for handling all the chat requests 
@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API endpoint to interact with the chatbot using LangGraph and tools. 
    Dynamically selects the model specifies in the request. 
    """
    
    if request.model_name not in MODEL_NAMES:
        return{"error": "Invalid model name. Please select a valid model."}
    
    # Initialize the LLM with the selected model 
    llm = ChatGroq(groq_api_key = groq_api_key, model_name= request.model_name)
    
    # Create a React agent using the selected LLM and tools 
    agent = create_react_agent(llm, tools= tools, state_modifier=request.model_name)
    
    # Create the initial state for processing
    state = {"messages": request.messages}

    # Process the state using the agent
    result = agent.invoke(state)  # Invoke the agent (can be async or sync based on implementation)

    # Return the result as the response
    return result

# Run the application if executed as the main script
if __name__ == '__main__':
    import uvicorn  # Import Uvicorn server for running the FastAPI app
    uvicorn.run(app, host='127.0.0.1', port=8000)  # Start the app on localhost with port 8000
    


