from pinecone import Pinecone, ServerlessSpec
import openai
import global_parameters_variables as gpv

# Initialize the Pinecone client
pc = Pinecone(api_key=gpv.API_KEY)
openai.api_key = gpv.OPENAI_API_KEY
index = pc.Index('pinecone-datacamp')

# Define a retrieve function that takes four arguments: query, top_k, namespace, and emb_model
def retrieve(query, top_k, namespace, emb_model):
    # Encode the input query using OpenAI
    query_response = openai.embeddings.create(
        input=query,
        model=emb_model
    )
    
    query_emb = query_response.data[0].embedding
    
    # Query the index using the query_emb
    docs = index.query(vector=query_emb, top_k=top_k, namespace=namespace, include_metadata=True)
    
    retrieved_docs = []
    sources = []
    for doc in docs['matches']:
        retrieved_docs.append(doc['metadata']['text'])
        sources.append((doc['metadata']['title'], doc['metadata']['url']))
    
    return retrieved_docs, sources

def prompt_with_context_builder(query, docs):
    delim = '\n\n---\n\n'
    prompt_start = 'Answer the question based on the context below.\n\nContext:\n'
    prompt_end = f'\n\nQuestion: {query}\nAnswer:'

    prompt = prompt_start + delim.join(docs) + prompt_end
    return prompt

def question_answering(prompt, sources, chat_model):
    sys_prompt = "You are a helpful assistant that always answers questions."
    
    # Use OpenAI chat completions to generate a response
    res = openai.chat.completions.create(
        model=chat_model,
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    answer = res.choices[0].message.content.strip()
    answer += "\n\nSources:"
    for source in sources:
        answer += "\n" + source[0] + ": " + source[1]
    
    return answer

documents, sources = retrieve(
  query="How to build next-level Q&A with OpenAI",
  top_k=3,
  namespace='youtube_rag_dataset',
  emb_model="text-embedding-3-small"
)
print(documents)
print(sources)