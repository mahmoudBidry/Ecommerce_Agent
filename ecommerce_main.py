from dotenv import load_dotenv
import os
from llama_index.llms.openai import OpenAI
from llama_index.core import Settings
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.core.memory import ChatMemoryBuffer
from load_text_data import text_engine
from ecommerce_prompts import ECOMMERCE_CONTEXT
from ecommerce_notes import ecommerce_notes_tool, ecommerce_notes_query

def initialize_agent():
    # Load environment variables
    load_dotenv()
    
    # Initialize OpenAI LLM
    llm = OpenAI(model="gpt-4o-mini-2024-07-18")
    Settings.llm = llm
    
    # Initialize chat memory
    memory = ChatMemoryBuffer.from_defaults(token_limit=2500)
    
    # Create tools
    tools = [
        QueryEngineTool(
            query_engine=text_engine,
            metadata=ToolMetadata(
                name="ecommerce_assistant",
                description="Use this tool to get information about products, prices, features, availability, shipping policies, and return policies."
            ),
        ),
        ecommerce_notes_tool,
        ecommerce_notes_query
    ]
    
    # Create ReAct agent with memory and system prompts
    agent = ReActAgent.from_tools(
        tools,
        llm=llm,
        verbose=True,
        context=ECOMMERCE_CONTEXT,
        memory=memory,
        system_prompt="You are a friendly e-commerce assistant. Stay focused on store-related topics."
    )
    
    return agent

def format_chat_history(chat_history):
    if not chat_history:
        return ""
    return "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in chat_history])

def main():
    # Initialize the agent
    agent = initialize_agent()
    chat_history = []
    
    print("E-commerce Customer Support AI Agent")
    print("===================================")
    print("Ask me anything about our products or policies (type 'quit' to exit)")
    
    while True:
        query = input("\nCustomer: ").strip()
        
        if query.lower() in ['quit', 'exit', 'q']:
            print("Thank you for using our customer support service. Goodbye!")
            break
            
        if not query:
            continue
        
        # Add user message to chat history
        chat_history.append({
            "role": "user",
            "content": query
        })
        
        # Get response while maintaining conversation history
        response = agent.query(query)
        
        # Add assistant response to chat history
        chat_history.append({
            "role": "assistant",
            "content": str(response)
        })
        
        # Update agent's memory using reset() and add_messages()
        agent.memory.reset()
        agent.memory.put(chat_history)
        
        print("\nAssistant:", response)

if __name__ == "__main__":
    main()
