from pinecone import Pinecone, ServerlessSpec
import global_parameters_variables as gpv
import functions

# Initialize the Pinecone client
# Initialize the Pinecone client
pc = Pinecone(api_key=gpv.API_KEY)
index = pc.Index('pinecone-datacamp')

query = "How to build next-level Q&A with OpenAI"

# Retrieve the top three most similar documents and their sources
documents, sources = functions.retrieve(query, top_k=3, namespace='youtube_rag_dataset', emb_model="text-embedding-3-small")

prompt_with_context = functions.prompt_with_context_builder(query, documents)
print(prompt_with_context)

answer = functions.question_answering(
  prompt=prompt_with_context,
  sources=sources,
  chat_model='gpt-4o-mini')
print(answer)