RAG_PROMPT = """
You are a real estate assistant.

User Query:
{query}

Available Properties:
{context}

Explain and recommend the best matching properties.
"""