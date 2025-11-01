from pinecone import Pinecone, ServerlessSpec
import global_parameters_variables as gpv

pc = Pinecone(api_key=gpv.API_KEY)

index = pc.Index(name='datacamp-index')

#update values pf vector ID 7
index.update(id="7", values = gpv.vector)

#fetch vector ID 7
fetched_vector = index.fetch(ids=["7"])
print(fetched_vector)


# Update the metadata of vector ID 7
index.update(
    id="7",
    set_metadata={"genre":"thriller", "year":2024}
)

# Fetch vector ID 7
fetched_vector = index.fetch(ids=["7"])
print(fetched_vector)