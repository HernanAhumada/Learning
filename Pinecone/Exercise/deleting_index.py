from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key='pcsk_2bDKwa_UwLPAepSK634J8wpHJ8YvyB5tcx3v5PBLbkSwpX4zDL6C2ETTGdPLViVKDByNqC')

pc.delete_index('my-first-index')

print(pc.list_indexes())