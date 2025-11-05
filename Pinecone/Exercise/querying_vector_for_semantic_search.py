from pinecone import Pinecone, ServerlessSpec
import pandas as pd
import numpy as np
from uuid import uuid4
import openai
import global_parameters_variables as gpv

# Initialize the Pinecone client
openai.api_key = gpv.OPENAI_API_KEY
pc = Pinecone(api_key=gpv.API_KEY)
index = pc.Index('pinecone-datacamp')

query = "What is in front of the Notre Dame Main Building?"

# Create the query vector
query_response = openai.embeddings.create(
    input=query,
    model="text-embedding-3-small"
)
query_emb = query_response.data[0].embedding

# Query the index and retrieve the top five most similar vectors
retrieved_docs = index.query(vector=query_emb, top_k=5, namespace='squad_dataset')

for result in retrieved_docs['matches']:
    print(f"{result['id']}: {round(result['score'], 2)}")
    print('\n')