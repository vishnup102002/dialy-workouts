# RAG Evolution Lab 🧠

A professional technical log documenting the development of robust, production-grade Retrieval-Augmented Generation (RAG) systems. This repository tracks the transition from basic pipelines to agentic, layout-aware AI architectures.

## 🚀 Lab Progress

### Day 1: Basic RAG Pipeline
*   **Focus:** MVP setup using standard text extraction and vector storage.
*   **Architecture:** Implemented core RAG flow: `TextLoader` -> `RecursiveCharacterTextSplitter` -> `ChromaDB` -> `Groq (Llama-3)`.
*   **Key Takeaway:** Understanding the fundamental dependency flow in LangChain.

### Day 2: Parent-Document Retrieval
*   **Focus:** Solving context fragmentation.
*   **Architecture:** Implemented `ParentDocumentRetriever` with distinct chunking strategies: 
    *   **Child Chunks:** Small, optimized for high-precision vector similarity.
    *   **Parent Chunks:** Large, optimized for LLM context (tables/flowcharts).
*   **Key Takeaway:** Hierarchical chunking significantly improves retrieval relevance for technical documentation.

### Day 3: Intelligent PDF Parsing & Framework Alignment
*   **Focus:** Handling complex layouts (tables/flowcharts) and framework interoperability.
*   **Key Implementations:**
    *   **LlamaParse Integration:** Replaced basic loaders with `LlamaParse` to convert visually dense PDFs into LLM-ready Markdown.
    *   **Adapter Pattern:** Built a bridge to convert `LlamaIndex` Document objects into `LangChain` Document objects (mapping `.text` to `.page_content`).
    *   **Persistence Management:** Solved vector store cross-contamination by isolating data into custom `Chroma` collections.

---

## 🛠 Framework Comparisons

### 1. PyMuPDF vs. LlamaParse
| Feature | PyMuPDF | LlamaParse |
| :--- | :--- | :--- |
| **Approach** | Rule-based, local text extraction. | Vision-Language Models (VLMs). |
| **Use Case** | High-speed, clean digital-native text. | Complex layouts, tables, charts. |
| **Architecture** | Purely local/offline. | Cloud-native API. |

### 2. LlamaIndex Document vs. LangChain Document
*   **LlamaIndex Document:** Structured as a "Node" with built-in graph relationships (`PREVIOUS`, `PARENT`). Optimized for deep indexing and advanced RAG orchestration.
*   **LangChain Document:** A lightweight, generic dictionary wrapper. Optimized for universal pipeline compatibility and multi-tool orchestration.
*   **Integration:** Since they differ, I implemented a manual converter: `Document(page_content=doc.text, metadata=doc.metadata)` to bridge the schema mismatch.

---

## 💡 Engineering Philosophy
I treat my data pipeline as a system, not just a script. By modularizing configurations (`parser_config.py`) and isolating vector stores, I ensure the system is maintainable, scalable, and professional.

*Maintained by Vishnu P.*
