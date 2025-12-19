from llm.llm_client import llm
from utils.prompt import RAG_PROMPT


def generate_answer(query, context):
    prompt = RAG_PROMPT.format(
        query=query,
        context="\n".join(context)
    )
    return llm.predict(prompt)
