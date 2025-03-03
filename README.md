# E-commerce Customer Support AI Agent

An intelligent customer support agent built with Python and LlamaIndex, designed to provide accurate product information and handle customer inquiries using RAG (Retrieval-Augmented Generation) technology.

## Project Overview

This project implements a customer support AI agent specifically designed for e-commerce applications. The agent can:
- Answer questions about products and their specifications
- Provide information about shipping and return policies
- Maintain conversation context for natural interactions
- Save and retrieve customer notes
- Process queries using a knowledge base of product catalogs and company policies

### Technical Architecture

The project uses a RAG (Retrieval-Augmented Generation) approach with the following components:

1. **Vector Store Index**: 
   - Products and policies are indexed using LlamaIndex
   - Enables semantic search and relevant information retrieval
   - Maintains persistent storage of indexed data

2. **Memory System**:
   - Implements chat history using ChatMemoryBuffer
   - Maintains conversation context
   - Supports natural follow-up questions

3. **Tool System**:
   - QueryEngineTool for accessing product and policy information
   - Note-taking tools for maintaining customer records
   - Extensible architecture for adding new capabilities

4. **LLM Integration**:
   - Uses OpenAI's GPT models for natural language understanding
   - Custom prompt templates for consistent responses
   - Context-aware query processing

## Prerequisites

- Python 3.11.11
- OpenAI API key
- pip package manager

## Installation

1. **Clone the Repository**
```bash
git clone <repository-url>
cd <repository-name>
```

2. **Create and Activate Virtual Environment**
```bash
python3.11 -m venv venv
# On Windows
.\venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Environment Setup**
Create a `.env` file in the project root:
```
OPENAI_API_KEY=your_api_key_here
```

## Project Structure

```
.
├── assessment_data/
│   ├── products.txt      # Product catalog
│   └── policies.txt      # Company policies
├── ecommerce_main.py     # Main application entry point
├── ecommerce_notes.py    # Note-taking functionality
├── ecommerce_prompts.py  # Prompt templates
├── load_text_data.py     # Data loading and indexing
└── requirements.txt      # Project dependencies
```

## Usage Guide

1. **Start the Agent**
```bash
python ecommerce_main.py
```

2. **Sample Questions and Responses**

The agent is trained with these example interactions:

```
Q: How much does the UltraPhone X cost?
A: The UltraPhone X costs $799. It's available in Black, Silver, and Blue colors.

Q: What are your shipping options?
A: We offer standard shipping (3-5 business days) for $4.99 and express shipping (1-2 business days) for $12.99. Orders over $50 qualify for free standard shipping.

Q: Can I return a laptop if I change my mind?
A: Yes, you can return a laptop within 30 days of purchase if it's in its original condition and packaging. A proof of purchase is required.

Q: When will the GamerPro 5 Laptop be available?
A: The GamerPro 5 Laptop is currently available for pre-order and will ship in 2 weeks.

Q: Do AirBuds Pro support wireless charging?
A: Yes, the AirBuds Pro support wireless charging and offer up to 24 hours of battery life.
```

3. **Example Interactions**

Here are some additional ways to interact with the agent:

```
Customer: What color options are available for the UltraPhone X?
Assistant: The UltraPhone X is available in Black, Silver, and Blue colors.

Customer: How much is express shipping?
Assistant: Express shipping costs $12.99 and takes 1-2 business days. However, if your order is over $50, you qualify for free standard shipping (3-5 business days).

Customer: Can you make a note that I prefer the blue UltraPhone?
Assistant: I'll add a note about your color preference.
Note saved successfully: Customer prefers the blue UltraPhone X.
```

4. **Available Commands**
- Type your question naturally
- Use 'quit', 'exit', or 'q' to end the session
- Ask about previous notes using "what are my recent notes?"

## Features

- **Contextual Understanding**: Maintains conversation history for natural dialog
- **Product Knowledge**: Detailed information about products, prices, and availability
- **Policy Information**: Shipping, returns, and other company policies
- **Note Taking**: Save and retrieve customer preferences and interaction history
- **Persistent Memory**: Conversation context is maintained throughout the session

## Technical Details

- Uses LlamaIndex 0.12.22 for vector storage and retrieval
- Implements ReAct agent pattern for tool usage
- Custom prompt templates for consistent response formatting
- Text-based storage for customer notes
- Memory buffer with 2500 token limit for conversation history

## Best Practices

- Ask specific questions about products or policies
- One question at a time for best results
- Use follow-up questions naturally
- Request notes for important preferences or details
