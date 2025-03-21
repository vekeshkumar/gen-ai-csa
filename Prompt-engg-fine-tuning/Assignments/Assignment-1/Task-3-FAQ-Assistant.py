from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.vectorstores import Pinecone

# Initialize vector store and retriever
vector_store = Pinecone.from_texts([...], embedding=OpenAIEmbeddings(), index_name="genspark-ai-course")
retriever = vector_store.as_retriever()

# Set up QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    retriever=retriever
)

# Streamlit UI
import streamlit as st

st.title("Genspark AI Course FAQ Assistant")
query = st.text_input("Ask a question about the course:")
if query:
    response = qa_chain.run(query)
    st.write(response)
