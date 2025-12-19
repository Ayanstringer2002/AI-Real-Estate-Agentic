# ✅ MUST be first
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from rag.retriever import retrieve_context
from rag.generator import generate_answer
from agents.planner import plan
from memory import chat_memory

st.set_page_config(page_title="Agentic AI Real Estate Assistant")
st.title("🏠 Agentic AI Real Estate Assistant")

# Sidebar Filters
st.sidebar.header("Filters")
min_budget, max_budget = st.sidebar.slider(
    "Budget Range (₹ in Lakhs)",
    min_value=10,
    max_value=500,
    value=(50, 150)
)

location = st.sidebar.selectbox(
    "Preferred Location",
    ["Any", "Bangalore", "Pune", "Hyderabad", "Mumbai", "Chennai", "Delhi", "Patna"]
)

query = st.chat_input("Describe your property needs")

if query:
    user_plan = plan(query)
    user_plan["budget_range"] = f"₹{min_budget}L – ₹{max_budget}L"
    user_plan["location_filter"] = location

    context = retrieve_context(query)
    generate_answer(query, context, user_plan)

# Render chat history
for msg in chat_memory.get():
    st.chat_message(msg["role"]).write(msg["content"])
