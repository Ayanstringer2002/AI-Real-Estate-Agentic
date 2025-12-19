# 🏠 AI Real Estate Assistant (Agentic RAG System)

An **Agentic AI-powered Real Estate Assistant** that helps buyers and renters discover properties using **natural language conversations**.  
The system combines **multi-agent planning**, **Retrieval-Augmented Generation (RAG)**, **conversational memory**, and **Groq** to deliver **personalized and explainable property recommendations**.

## 🚀 Features

- 💬 **Conversational Property Search**  
  Search for properties using natural language queries with an interactive chat interface.

- 🧠 **Agentic Planning System**  
  Intelligent coordination between **Budget**, **Location**, and **Lifestyle** agents to generate personalized results.

- 🔍 **Semantic Search**  
  High-quality vector search powered by **FastEmbed** and **ChromaDB** for context-aware property retrieval.

- 🤖 **LLM-Based Reasoning**  
  Uses **Groq LLM** to generate accurate, human-like, and reasoned property recommendations.

- 🧾 **Explainable AI Outputs**  
  Clear explanations on *why* a property matches the user’s preferences and constraints.

- 🧠 **Conversational Memory**  
  Maintains multi-turn chat history for coherent and context-aware conversations.

- 🎛️ **Interactive UI Filters**  
  User-friendly controls for budget, location, and preference-based filtering.

## 🏗️ System Architecture

The AI Real Estate Assistant is built using an agentic, retrieval-augmented architecture designed for intelligent, explainable, and conversational property discovery.

User Query
↓
Streamlit UI (Filters + Chat)
↓
Planner Agent
├── Budget Agent
├── Location Agent
└── Lifestyle Agent
↓
RAG Pipeline
├── FastEmbed (Embeddings)
└── ChromaDB (Vector Store)
↓
Groq LLM (Reasoning & Response Generation)
↓
Conversational Memory
↓
Explainable Property Recommendations


### 🔍 Architecture Breakdown

- **Streamlit UI**  
  Interactive interface supporting chat-based search and UI filters (budget, location, preferences).

- **Planner Agent**  
  Orchestrates multiple specialized agents to break down user intent.

- **Specialized Agents**
  - **Budget Agent** → Enforces affordability constraints  
  - **Location Agent** → Filters based on geographic preferences  
  - **Lifestyle Agent** → Considers amenities, commute, and lifestyle needs

- **RAG Pipeline**
  - **FastEmbed** for generating semantic embeddings  
  - **ChromaDB** for efficient vector-based property retrieval

- **Groq LLM**
  - High-performance LLM used for reasoning, ranking, and natural language responses

- **Conversational Memory**
  - Maintains context across multi-turn conversations

- **Explainable Recommendations**
  - Clearly explains *why* a property matches the user’s requirements




