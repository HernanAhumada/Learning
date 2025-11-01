from pinecone import Pinecone, ServerlessSpec

pc=Pinecone(api_key='pcsk_2bDKwa_UwLPAepSK634J8wpHJ8YvyB5tcx3v5PBLbkSwpX4zDL6C2ETTGdPLViVKDByNqC')

#connect to the index
index = pc.Index(name='my-first-index')
print(index.describe_index_stats())