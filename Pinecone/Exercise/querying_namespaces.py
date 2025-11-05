from pinecone import Pinecone, ServerlessSpec
import global_parameters_variables as gpv

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=gpv.API_KEY)

index = pc.Index('datacamp-index')

# Query namespace1 with the vector provided
query_result = index.query(vector=gpv.vector, top_k=3, namespace='namespace1')
print(query_result)