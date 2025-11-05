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

batch_limit = 100

df = pd.read_csv('C:/Users/User/Documents/REPOSITORY/Learning/Pinecone/squad_dataset.csv')

for batch in np.array_split(df, len(df) / batch_limit):
    # Extract the metadata from each row
    metadatas = [{
      "text_id": row['id'],
      "text": row['text'],
      "title": row['title']} for _, row in batch.iterrows()]
    texts = batch['text'].tolist()
    
    ids = [str(uuid4()) for _ in range(len(texts))]
    
    # Encode texts using OpenAI
    response = openai.Embedding.create(input=texts, model="text-embedding-3-small")
    embeds = [np.array(x.embedding) for x in response.data]
    
    # Upsert vectors to the correct namespace
    index.upsert(vectors=zip(ids, embeds, metadatas), namespace='squad_dataset')