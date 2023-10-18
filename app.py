import os
from dotenv import load_dotenv
from llama_index import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    ServiceContext,
)
from llama_index.llms import PaLM
from langchain.embeddings.google_palm import GooglePalmEmbeddings

load_dotenv()

model = "models/text-bison-001"
embeddings = GooglePalmEmbeddings(google_api_key=os.getenv("PALM_API_KEY"))

documents = SimpleDirectoryReader("data").load_data()

llm = PaLM(api_key=os.getenv("PALM_API_KEY"), model_name=model)
service_context = ServiceContext.from_defaults(llm=llm, embed_model=embeddings)

index = VectorStoreIndex.from_documents(documents, service_context=service_context)

query_engine = index.as_query_engine()
response = query_engine.query("What is the moral of the story")
print(response)
