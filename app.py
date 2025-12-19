import streamlit as st
from rag.retriever import retrieve_context
from rag.generator import generate_answer
from agents.planner import plan
from memory.chat_memory import memory

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
    ["Any", "Bangalore", "Pune", "Hyderabad", "Mumbai", "Chennai"]
)

query = st.chat_input("Describe your property needs")

if query:
    user_plan = plan(query)
    user_plan["budget_range"] = f"₹{min_budget}L – ₹{max_budget}L"
    user_plan["location_filter"] = location

    context = retrieve_context(query)
    response = generate_answer(query, context, user_plan)

for msg in memory.chat_memory.messages:
    role = "User" if msg.type == "human" else "Assistant"
    st.chat_message(role).write(msg.content)