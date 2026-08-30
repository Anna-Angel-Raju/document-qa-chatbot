"""
RAG answer generation logic.
"""

def ask_rag(question, context):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a precise question-answering assistant. "
                "Answer ONLY using the information in the provided context. "
                "If the answer is not in the context, respond exactly with: "
                "\"I couldn't find this information.\" "
                "Do not guess, infer, or add any detail not explicitly stated in the context. "
                "Be concise and directly answer what is asked."
            )
        },
        {
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion: {question}"
        }
    ]

    output = llm_pipeline(
        messages,
        max_new_tokens=150,
        do_sample=False,
        temperature=None,
        top_p=None,
    )

    return output[0]["generated_text"][-1]["content"]
