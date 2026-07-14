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

load_dotenv()

# Setup API Key
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("Missing API Key! Ensure it is set in your .env file.")

# 1. Load local file
loader = TextLoader("data/data.txt")
docs = loader.load()

# 2. Split it into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_documents(docs)

# 3. Create Vector Store
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(documents=texts, embedding=embeddings)

# 4. Setup LLM
llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama-3.3-70b-versatile"
)

def get_ans(question, tone="professional"):
    # 5. Modern Retrieval Chain (The "LCEL" way)
    prompt = ChatPromptTemplate.from_template(
        f"You are a helpful assistant. Please answer in a {tone} tone. "
        "Context: {context} "
        "Question: {input}"
    )
    
    # Create the chain
    combine_docs_chain = create_stuff_documents_chain(llm, prompt)
    retrieval_chain = create_retrieval_chain(vectorstore.as_retriever(), combine_docs_chain)
    
    # Invoke
    response = retrieval_chain.invoke({"input": question})
    return response["answer"]

# Run
print(get_ans("What is the main topic of the document?", tone="pirate"))