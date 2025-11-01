from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key='pcsk_2bDKwa_UwLPAepSK634J8wpHJ8YvyB5tcx3v5PBLbkSwpX4zDL6C2ETTGdPLViVKDByNqC')

index = pc.Index('datacamp-index')
ids = ['2', '5']

fetched_vectors = index.fetch(ids=ids) #returns and object FetchResponse
#fetched_vectors_dict = fetched_vectors.to_dict() #convert the FetchResponse object to a Dictionary

#extract the metadata from each result in fetched_vectors
metadatas = [fetched_vectors.vectors[id].metadata for id in ids]
print(metadatas)

print(index.describe_index_stats())