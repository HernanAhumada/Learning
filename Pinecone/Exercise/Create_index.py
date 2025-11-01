# Import the Pinecone library
from pinecone import Pinecone, ServerlessSpec 

# Initialize the Pinecone client
pc = Pinecone(api_key="pcsk_2bDKwa_UwLPAepSK634J8wpHJ8YvyB5tcx3v5PBLbkSwpX4zDL6C2ETTGdPLViVKDByNqC")

pc.delete_index(name="my-first-index")
#pc.delete_index(name="hernan-first-index")

if not pc.has_index('my-first-index'):
    pc.create_index(
        name='my-first-index',
        dimension=1536,
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )

print(pc.list_indexes())