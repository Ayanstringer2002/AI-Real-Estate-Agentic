from llm.llm_client import generate_llm_response
from utils.prompt import RAG_PROMPT
from memory.chat_memory import memory

def generate_answer(query, context, plan):
    prompt = RAG_PROMPT.format(
        query=query,
        context="\n".join(context),
        plan=plan
    )

    response = generate_llm_response(prompt)
    memory.save_context({"input": query}, {"output": response})
    return response
