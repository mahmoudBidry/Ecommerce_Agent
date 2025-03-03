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

The example interactions demonstrate the agent's capabilities through a detailed conversation that shows:

**Conversation Format**:
- `Customer:` - User inputs are clearly marked
- `>` - Shows the internal reasoning process (can be hidden in production)
- `Thought:` - The agent's step-by-step reasoning
- `Action:` - The tool or method being called
- `Action Input:` - The specific query or parameters
- `Observation:` - The result from the tool
- `Answer:` or `A:` - The final response to the user

**Reasoning Process (ReAct Pattern)**:
The agent follows a structured reasoning pattern:
1. Analyzes the user's request
2. Formulates a plan using internal thoughts
3. Decides which tools to use (ecommerce_assistant, add_customer_note, etc.)
4. Processes the results
5. Generates a natural language response

This reasoning process is visible in the example where the agent:
- Lists all products
- Compares products and saves notes
- Checks return policies
- Retrieves customer notes

The example shows how the agent handles:
- Complex queries requiring multiple steps
- Information retrieval and comparison
- Note-taking and memory access
- Policy verification
- Natural follow-up questions

Here are some additional ways to interact with the agent:

```
E-commerce Customer Support AI Agent
===================================
Ask me anything about our products or policies (type 'quit' to exit)

Customer: give me all products              
> Running step 5c2575d2-b507-4942-8220-29baab98426d. Step input: give me all products
Thought: The user is asking for a list of all products. I need to use the ecommerce_assistant tool to retrieve this information.
Action: ecommerce_assistant
Action Input: {'input': 'list all products'}
Observation: Here are the products we currently have available:

1. UltraPhone X
   Price: $799
   Features: 6.5" OLED display, 128GB storage, 12MP camera
   Colors: Black, Silver, Blue
   Availability: In stock

2. MaxBook Pro 14
   Price: $1,299
   Features: 14" Retina display, 512GB SSD, M2 chip
   Colors: Silver, Space Gray
   Availability: Out of stock

3. AirBuds Pro
   Price: $199
   Features: Noise cancellation, wireless charging, 24-hour battery life
   Colors: White, Black
   Availability: In stock

4. SmartWatch Elite
   Price: $349
   Features: AMOLED display, heart rate monitor, GPS tracking
   Colors: Black, Rose Gold, Silver
   Availability: In stock

5. GamerPro 5 Laptop
   Price: $2,499
   Features: 15.6" 144Hz display, RTX 4070 GPU, 1TB SSD, 32GB RAM
   Colors: Black, Red
   Availability: Pre-order (ships in 2 weeks)

Is there anything else I can assist you with?
> Running step 0325851f-03b4-42eb-91e5-e87a2e59588a. Step input: None
Thought: I can answer without using any more tools. I'll use the user's language to answer.
Answer: Here are the products we currently have available:

1. **UltraPhone X**
   - Price: $799
   - Features: 6.5" OLED display, 128GB storage, 12MP camera
   - Colors: Black, Silver, Blue
   - Availability: In stock

2. **MaxBook Pro 14**
   - Price: $1,299
   - Features: 14" Retina display, 512GB SSD, M2 chip
   - Colors: Silver, Space Gray
   - Availability: Out of stock

3. **AirBuds Pro**
   - Price: $199
   - Features: Noise cancellation, wireless charging, 24-hour battery life
   - Colors: White, Black
   - Availability: In stock

4. **SmartWatch Elite**
   - Price: $349
   - Features: AMOLED display, heart rate monitor, GPS tracking
   - Colors: Black, Rose Gold, Silver
   - Availability: In stock

5. **GamerPro 5 Laptop**
   - Price: $2,499
   - Features: 15.6" 144Hz display, RTX 4070 GPU, 1TB SSD, 32GB RAM
   - Colors: Black, Red
   - Availability: Pre-order (ships in 2 weeks)

Is there anything else I can assist you with?

Assistant: Here are the products we currently have available:

1. **UltraPhone X**
   - Price: $799
   - Features: 6.5" OLED display, 128GB storage, 12MP camera
   - Colors: Black, Silver, Blue
   - Availability: In stock

2. **MaxBook Pro 14**
   - Price: $1,299
   - Features: 14" Retina display, 512GB SSD, M2 chip
   - Colors: Silver, Space Gray
   - Availability: Out of stock

3. **AirBuds Pro**
   - Price: $199
   - Features: Noise cancellation, wireless charging, 24-hour battery life
   - Colors: White, Black
   - Availability: In stock

4. **SmartWatch Elite**
   - Price: $349
   - Features: AMOLED display, heart rate monitor, GPS tracking
   - Colors: Black, Rose Gold, Silver
   - Availability: In stock

5. **GamerPro 5 Laptop**
   - Price: $2,499
   - Features: 15.6" 144Hz display, RTX 4070 GPU, 1TB SSD, 32GB RAM
   - Colors: Black, Red
   - Availability: Pre-order (ships in 2 weeks)

Is there anything else I can assist you with?

Customer: compare the third product with SmartWatch Elite, and save the result in the note
> Running step d6a39da1-0c65-4389-8189-283827d3c4cc. Step input: compare the third product with SmartWatch Elite, and save the result in the note
Thought: I need to retrieve information about the third product and the SmartWatch Elite to compare them. I'll start by getting details about the SmartWatch Elite first.
Action: ecommerce_assistant
Action Input: {'input': 'SmartWatch Elite'}
Observation: The SmartWatch Elite is priced at $349 and comes in Black, Rose Gold, and Silver colors. It features an AMOLED display, heart rate monitor, and GPS tracking. It is currently in stock and available for purchase. If you have any further questions or need assistance with anything else, feel free to ask!
> Running step a664e85b-5122-4c92-8634-0c224e8752f8. Step input: None
Thought: Now that I have the details for the SmartWatch Elite, I need to find information about the third product to make a comparison. I'll retrieve the details for the third product now.
Action: ecommerce_assistant
Action Input: {'input': 'third product'}
Observation: The third product is the AirBuds Pro. They are priced at $199 and come with features like noise cancellation, wireless charging, and a 24-hour battery life. They are available in White and Black colors and are currently in stock. If you're interested in purchasing them, you can add them to your cart and choose your preferred shipping option. If you have any more questions or need assistance with anything else, feel free to let me know!
> Running step a186d265-61a6-453b-97f3-6beea67bd1c7. Step input: None
Thought: I now have the information for both products. I will compare the SmartWatch Elite and the AirBuds Pro and save the result in a note. 
Here’s the comparison:

- **SmartWatch Elite**
  - Price: $349
  - Colors: Black, Rose Gold, Silver
  - Features: AMOLED display, heart rate monitor, GPS tracking
  - Availability: In stock

- **AirBuds Pro**
  - Price: $199
  - Colors: White, Black
  - Features: Noise cancellation, wireless charging, 24-hour battery life
  - Availability: In stock

Now, I will save this comparison in a note.
Action: add_customer_note
Action Input: {'content': 'Comparison between SmartWatch Elite and AirBuds Pro:\n\n- SmartWatch Elite:\n  - Price: $349\n  - Colors: Black, Rose Gold, Silver\n  - Features: AMOLED display, heart rate monitor, GPS tracking\n  - Availability: In stock\n\n- AirBuds Pro:\n  - Price: $199\n  - Colors: White, Black\n  - Features: Noise cancellation, wireless charging, 24-hour battery life\n  - Availability: In stock', 'category': 'comparison'}
Observation: Note saved successfully: Comparison between SmartWatch Elite and AirBuds Pro:

- SmartWatch Elite:
  - Price: $349
  - Colors: Black, Rose Gold, Silver
  - Features: AMOLED display, heart rate monitor, GPS tracking
  - Availability: In stock

- AirBuds Pro:
  - Price: $199
  - Colors: White, Black
  - Features: Noise cancellation, wireless charging, 24-hour battery life
  - Availability: In stock
> Running step d5b03ae0-5766-4e9f-bfc9-d83e5f20c3f1. Step input: None
Thought: I have successfully saved the comparison note between the SmartWatch Elite and the AirBuds Pro.
Answer: The comparison has been saved, and if you need any further assistance or have more questions, feel free to ask!

Assistant: The comparison has been saved, and if you need any further assistance or have more questions, feel free to ask!

Customer: thanks, I have bought a smartwatch 40 days ago can I return it?
> Running step 13310c78-a0f5-4b66-9385-2c0b2c67091e. Step input: thanks, I have bought a smartwatch 40 days ago can I return it?
Thought: The user is inquiring about the return policy for a smartwatch purchased 40 days ago. I need to check the return policy details to provide an accurate answer.
Action: ecommerce_assistant
Action Input: {'input': 'return policy for smartwatch'}
Observation: Our return policy for the SmartWatch Elite is as follows:
- Returns are accepted within 30 days of purchase with proof of purchase.
- The item must be in its original condition and packaging.
- Refunds are processed within 5 business days of receiving the returned item.
- Please note that digital products and personalized items are non-refundable.

If you have any further questions or need assistance with your return, feel free to let us know!
> Running step 4b1d2714-45b3-4408-a6de-d9d2b428cc79. Step input: None
Thought: I have the information regarding the return policy for the smartwatch. Since the user purchased it 40 days ago, it falls outside the return window.
Answer: Unfortunately, you cannot return the smartwatch as it must be returned within 30 days of purchase. Since it has been 40 days, the return policy does not allow for a return.

Assistant: Unfortunately, you cannot return the smartwatch as it must be returned within 30 days of purchase. Since it has been 40 days, the return policy does not allow for a return.

Customer: what are my recent notes?
> Running step f94ec645-cdf4-4dd9-bf39-136e9b4fb9d2. Step input: what are my recent notes?
Thought: The user wants to retrieve their recent notes. I will use the get_recent_notes tool to do this.
Action: get_recent_notes
Action Input: {'limit': 5}
Observation: - AirBuds Pro:
  - Price: $199
  - Colors: White, Black
  - Features: Noise cancellation, wireless charging, 24-hour battery life
  - Availability: In stock

> Running step b86566f6-74c1-467a-bea9-445aed21f40a. Step input: None
Thought: I can answer without using any more tools. I'll use the user's language to answer.
Answer: Your recent notes include information about the AirBuds Pro: they are priced at $199, available in White and Black colors, feature noise cancellation and wireless charging, and have a 24-hour battery life. They are currently in stock.

Assistant: Your recent notes include information about the AirBuds Pro: they are priced at $199, available in White and Black colors, feature noise cancellation and wireless charging, and have a 24-hour battery life. They are currently in stock.

Customer: exit
Thank you for using our customer support service. Goodbye!
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
