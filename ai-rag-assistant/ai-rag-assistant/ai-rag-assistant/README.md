AI RAG Assistant 
Overview

Built a Retrieval-Augmented Generation (RAG) system that answers questions from PDF documents.

Features
Semantic search using sentence embeddings
PDF text extraction
Context-based answer generation
Interactive UI with Streamlit
Tech Stack
Python
Streamlit
Sentence Transformers
Scikit-learn
How it Works
PDF is split into chunks
Each chunk is converted into embeddings
Query is matched with most relevant chunks
Answer is generated from context

Run Locally
streamlit run app.py
