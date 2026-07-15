# RAG Evolution Lab 🧠

This folder documents my daily engineering journey in building robust Retrieval-Augmented Generation (RAG) systems. Instead of "vibe coding" in isolation, I am iterating on architectural patterns to solve real-world document retrieval challenges.

## 🚀 Lab Progress

### Day 1: Basic RAG Implementation
* **Focus:** Establishing the core RAG pipeline.
* **Architecture:** Implemented a standard RAG flow using `RecursiveCharacterTextSplitter`, `ChromaDB` for vector storage, and `Groq (Llama-3)` for generation.
* **Key Takeaway:** Understanding the dependency flow between document loaders, embedding models, and LLM orchestration via LangChain.

### Day 2: Parent-Document Retrieval (Chunking Strategy)
* **Focus:** Solving context loss in small-chunk retrieval.
* **Architecture:** Transitioned from a flat chunking strategy to a **Parent-Document Retrieval** pattern.
    * **Child Chunks (200 chars):** Used for high-precision semantic search.
    * **Parent Chunks (1000 chars):** Passed to the LLM to preserve full surrounding context during generation.
* **Key Takeaway:** Learned that intelligent chunking is superior to brute-forcing context windows. Document structure and retrieval granularity directly impact the accuracy of the AI's output.

## 🛠 Tech Stack
* **Orchestration:** LangChain (LCEL)
* **Inference:** Groq API (`llama-3.3-70b-versatile`)
* **Embeddings:** HuggingFace `all-MiniLM-L6-v2`
* **Storage:** ChromaDB, `InMemoryStore`

## ⚙️ Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment:**
   Create a `.env` file in this directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

3. **Run the Script:**
   ```bash
   python main.py
   ```

## 💡 Engineering Philosophy
Every script in this lab is reviewed, tested, and documented. I prioritize **modular architecture** (e.g., separating `parser_config.py` from `main.py`) to ensure that the code is maintainable and production-ready.

---
*Maintained by Vishnu P.*
