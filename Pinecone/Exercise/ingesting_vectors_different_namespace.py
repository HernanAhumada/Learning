from pinecone import Pinecone, ServerlessSpec
import global_parameters_variables as gpv

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=gpv.API_KEY)
index = pc.Index('datacamp-index')

# Upsert vector_set1 to namespace1
index.upsert(
  vectors=vector_set1,
  namespace='namespace1'
)

# Upsert vector_set2 to namespace2
index.upsert(
  vectors=vector_set2,
  namespace='namespace2'
)

# Print the index statistics
print(index.describe_index_stats())