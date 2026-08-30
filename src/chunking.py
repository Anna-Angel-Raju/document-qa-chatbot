"""
Chunking strategies used by the document QA system.
"""

def build_fixed_chunking_retriever(chunk_size=500, k=4):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=0,
        separators=["\n\n", "\n", ".", " ", ""],
    )
    chunks = splitter.split_documents(raw_documents)

    vectorstore = FAISS.from_documents(chunks, embedding_model)
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k}
    )
    print(f"[Fixed Chunking] Created {len(chunks)} chunks (size={chunk_size}, overlap=0)")
    return retriever




def build_overlap_chunking_retriever(chunk_size=500, chunk_overlap=100, k=4):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,   # e.g. 100 tokens/chars of overlap between consecutive chunks
        separators=["\n\n", "\n", ".", " ", ""],
    )
    chunks = splitter.split_documents(raw_documents)

    vectorstore = FAISS.from_documents(chunks, embedding_model)
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k}
    )
    print(f"[Overlap Chunking] Created {len(chunks)} chunks (size={chunk_size}, overlap={chunk_overlap})")
    return retriever




from langchain_experimental.text_splitter import SemanticChunker

def build_semantic_chunking_retriever(breakpoint_threshold_amount=80, k=4):
    semantic_splitter = SemanticChunker(
        embedding_model,
        breakpoint_threshold_type="percentile",     # splits where semantic similarity drops
        breakpoint_threshold_amount=breakpoint_threshold_amount,
    )
    chunks = semantic_splitter.split_documents(raw_documents)

    vectorstore = FAISS.from_documents(chunks, embedding_model)
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k}
    )
    print(f"[Semantic Chunking] Created {len(chunks)} chunks")
    return retriever
