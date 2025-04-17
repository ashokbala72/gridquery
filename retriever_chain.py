from dotenv import load_dotenv
import os
import openai

# Load from .env
load_dotenv()

# Get the key
openai.api_key = os.getenv("OPENAI_API_KEY")


openai.api_key = os.getenv("OPENAI_API_KEY")
from langchain.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document
import pandas as pd

def build_chain():
    df = pd.read_csv("grid_events_sample.csv")
    logs = []
    for _, row in df.iterrows():
        logs.append(f"[{row['timestamp']}] {row['substation']} | Load: {row['load_mw']} MW | Event: {row['event']}")
    text = "\n".join(logs)

    splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=20)
    documents = splitter.split_documents([Document(page_content=text)])

    embeddings = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(documents, embedding=embeddings, persist_directory="./chroma_grid")

    llm = ChatOpenAI(model="gpt-4-turbo")
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever())

    return qa
