from pinecone import Pinecone, ServerlessSpec
import global_parameters_variables as gpv
import utilities as u

pc = Pinecone(api_key=gpv.API_KEY)
# Upsert vectors in batches of 2 vectors
with pc.Index('datacamp-index', pool_threads=20) as index:
    async_results = [index.upsert(vectors=chunk, async_req=True) for chunk in u.chunks(gpv.vectors,2)]
    [async_result.get() for async_result in async_results]

print(index.describe_index_stats())