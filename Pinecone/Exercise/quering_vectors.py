from pinecone import Pinecone, ServerlessSpec
import global_parameters_variables as gpv

pc = Pinecone(api_key=gpv.API_KEY)

index = pc.Index(name='datacamp-index')

vector = gpv.vector

query_results = index.query(vector= vector, top_k=3)
print(query_results)

#FILTERING
# Retrieve the MOST similar vector with the year 2024
query_result = index.query(
    vector=vector,
    filter={'year': {'$eq':2024}},
    top_k=1,
    include_metadata=True
)
print(query_result)

# Retrieve the MOST similar vector with genre and year filters
query_result = index.query(
    vector = vector,
    filter = {
        "genre":"thriller",
        "year":{"$lt":2018}
    },
    top_k=1,
    include_metadata=True
)
print(query_result)