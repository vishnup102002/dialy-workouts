import os
from dotenv import load_dotenv

# 1. Imports
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

# 2. Modern Imports for Chains
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.retrievers import ParentDocumentRetriever
from langchain_core.stores import InMemoryStore
from parser_config import get_splitter_config
load_dotenv()

#  Setup Storage for Parent Documents
store = InMemoryStore()
# 1. Setup API and LLM
api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(groq_api_key=api_key, model_name="llama-3.3-70b-versatile")

# 2. Setup Vectorstore and Retriever
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma(embedding_function=embeddings)
store = InMemoryStore()
parent_splitter, child_splitter = get_splitter_config()

retriever = ParentDocumentRetriever(
    vectorstore=vectorstore,
    docstore=store,
    child_splitter=child_splitter,
    parent_splitter=parent_splitter
)

# Load data and add to retriever
loader = TextLoader("data/data.txt")
docs = loader.load()
retriever.add_documents(docs)

# 3. Create Chain
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please answer in a {tone} tone. Context: {context}"),
    ("human", "{input}")
])

combine_docs_chain = create_stuff_documents_chain(llm, prompt)
retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)

# 4. Function
def get_ans(question, tone="professional"):
    return retrieval_chain.invoke({"input": question, "tone": tone})["answer"]

# Run
print(get_ans("What is the main topic of the document?", tone="pirate"))