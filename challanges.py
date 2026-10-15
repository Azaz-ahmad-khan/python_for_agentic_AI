def count_by_role(messages):
    count={}
    for m in messages:
        role=m['role']
        count[role]=count.get(role,0)+1

    return count;    
        








messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is RAG?"},
    {"role": "assistant", "content": "Retrieval-Augmentead Generation combines search with an LLM."},
    {"role": "user", "content": "Explain chunking"},
    {"role": "assistant", "content": "Chunking splits documents into smaller pieces."},
    {"role": "user", "content": ""},
    {"role": "user", "content": "What is LangGraph?"},
]
print(count_by_role(messages=messages))