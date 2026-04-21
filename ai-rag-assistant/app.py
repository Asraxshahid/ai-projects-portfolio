import streamlit as st
import PyPDF2
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

st.title("AI PDF Assistant")

# Load modell
model = SentenceTransformer('all-MiniLM-L6-v2')

# Memory
if "history" not in st.session_state:
    st.session_state.history = []

# Read PDF
def read_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Chunk text
def chunk_text(text, chunk_size=120):
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

# Retrieve relevant chunks
def retrieve(query, chunks):
    query_embedding = model.encode([query])
    chunk_embeddings = model.encode(chunks)

    similarities = cosine_similarity(query_embedding, chunk_embeddings)[0]
    top_indices = np.argsort(similarities)[-3:]

    return [chunks[i] for i in top_indices]

# SIMPLE answer generator (stable)
def generate_answer(query, chunks):
    combined = " ".join(chunks)

    sentences = combined.split(".")
    results = [s for s in sentences if any(word in s.lower() for word in query.lower().split())]

    if results:
        return ". ".join(results[:2])
    else:
        return "Relevant information found but could not form exact answer."

# UI
query = st.text_input("Ask something:")
uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    text = read_pdf(uploaded_file)
    chunks = chunk_text(text)
    st.success("PDF processed")

    if query:
        top_chunks = retrieve(query, chunks)
        answer = generate_answer(query, top_chunks)

        st.session_state.history.append((query, answer))

        st.subheader("Answer")
        st.write(answer)

# History
if st.session_state.history:
    st.subheader("History")
    for q, a in reversed(st.session_state.history):
        st.write(f"**You:** {q}")
        st.write(f"**AI:** {a}")
