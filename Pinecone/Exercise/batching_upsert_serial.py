from pinecone import Pinecone, ServerlessSpec
import global_parameters_variables as gpv
import utilities as u

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=gpv.API_KEY)

index = pc.Index('datacamp-index')

# Upsert vectors in batches of 100
for chunk in u.chunks(gpv.vectors, 2):
    index.upsert(vectors=chunk)

# Retrieve statistics of the connected Pinecone index
print(index.describe_index_stats())