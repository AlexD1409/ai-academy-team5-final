from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from openai import AzureOpenAI
from typing import List, Dict

# --- Embedding Generation ---
def create_embedding(text: str, embedding_client: AzureOpenAI) -> List[float]:
    response = embedding_client.embeddings.create(input=text, model="azure/text-embedding-3-small")
    return response.data[0].embedding

# --- Vector Search ---
def vector_search(query: str, vector_client: SearchClient, embedding_client: AzureOpenAI, top_k: int = 5) -> List[Dict]:
    embedding = create_embedding(query, embedding_client)
    results = vector_client.search(
        search_text=None,
        vector_queries=[{
            "vector": embedding,
            "k": top_k,
            "fields": "embedding",
            "kind": "vector"
        }]
    )
    return list(results)

# --- Keyword Search ---
def keyword_search(query: str, keyword_client: SearchClient, top_k: int = 50) -> List[Dict]:
    results = keyword_client.search(
        search_text=query,
        top=top_k,
        include_total_count=True
    )
    return list(results)

# --- LLM Completion ---
def basic_llm_response(prompt: str, chat_client: AzureOpenAI, system_prompt) -> str:
    response = chat_client.chat.completions.create(
        model="azure/o4-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

###These are for updating the LLM system prompt
def load_prompt(file_path):
    with open(file_path,'r') as f:
        return f.read()
    
def save_prompt(file_path, data):
    with open(file_path, 'w') as f:
        f.write(data)
