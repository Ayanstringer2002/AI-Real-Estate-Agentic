from llm.llm_client import generate_llm_response
from utils.prompt import RAG_PROMPT
from memory import chat_memory

def generate_answer(query, context, plan):
    prompt = RAG_PROMPT.format(
        query=query,
        context="\n".join(context),
        plan=plan
    )

    response = generate_llm_response(prompt)

    # Save conversation
    chat_memory.add("user", query)
    chat_memory.add("assistant", response)

    return response

