from pinecone import Pinecone, ServerlessSpec
import global_parameters_variables as gpv

pc = Pinecone(api_key=gpv.API_KEY)

index = pc.Index('datacamp-index')

# Delete vectors
index.delete(ids=["8","1"])

# Retrieve metrics of the connected Pinecone index
print(index.describe_index_stats())
