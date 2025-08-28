print("📦 Script started")

from src.helper import load_pdf_file, text_spilt, download_hugging_face_embeddings
# from pinecone.grpc import PineconeGRPC as Pinecone

from pinecone import ServerlessSpec
from pinecone import Pinecone, ServerlessSpec

from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get API key
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

# Load and chunk PDF data
extracted_data = load_pdf_file(data='data/')
text_chunks = text_spilt(extracted_data)
print("Length of chunks:", len(text_chunks))

# Download embedding model
embeddings = download_hugging_face_embeddings()

# Init Pinecone client
pc = Pinecone(PINECONE_API_KEY)
index_name = "hexanovabot"

# Create index only if it doesn't exist
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,
        metric='cosine',
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )

# Store embeddings
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings,
)

print("✅ Successfully stored documents in Pinecone.")
