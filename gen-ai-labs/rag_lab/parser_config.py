from langchain_text_splitters import RecursiveCharacterTextSplitter

def get_splitter_config():
    """
    Returns the configuration for parent and child document splitting.
    
    Strategy:
    - Child chunks are small to ensure high-precision semantic search.
    - Parent chunks are large enough to contain tables and full paragraph context.
    """
    child_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200, 
        chunk_overlap=20
    )
    parent_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=100
    )
    return parent_splitter, child_splitter
