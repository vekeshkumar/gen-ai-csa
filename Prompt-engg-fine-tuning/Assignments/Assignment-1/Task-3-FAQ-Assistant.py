import streamlit as st
import openai
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


openai.api_key = "API KEY "


faq_data = {
    "What are the Gen Spark AI courses about?": "Gen Spark AI courses provide comprehensive training in various aspects of Artificial Intelligence, including machine learning, deep learning, and natural language processing.",
    "What are the prerequisites for Gen Spark AI courses?": "The prerequisites vary depending on the specific course. Generally, a basic understanding of programming (preferably Python) and some mathematical concepts (like linear algebra and calculus) is recommended.",
    "How long are the Gen Spark AI courses?": "The duration of Gen Spark AI courses can range from a few weeks to several months, depending on the course level and specialization.",
    "What is the cost of Gen Spark AI courses?": "The cost varies depending on the course. Please visit our website or contact our admissions team for the most up-to-date pricing information.",
    "What learning platform do you use for Gen Spark AI courses?": "We primarily use a combination of online learning platforms, including interactive video lectures, coding exercises on platforms like Jupyter Notebooks, and community forums.",
    "Do you offer any certifications upon completion of Gen Spark AI courses?": "Yes, upon successful completion of a Gen Spark AI course, you will receive a certificate of completion.",
    "Are the Gen Spark AI courses suitable for beginners?": "We offer courses for various skill levels, including introductory courses suitable for beginners with a basic understanding of technology.",
    "How are the courses structured?": "Our courses typically involve a mix of theoretical concepts, practical coding exercises, real-world case studies, and projects.",
    "Who are the instructors for Gen Spark AI courses?": "Our instructors are experienced AI professionals and researchers with a passion for teaching and mentoring.",
    "What kind of support do you offer to students?": "We provide comprehensive student support, including access to instructors through Q&A sessions, dedicated community forums, and technical assistance."
}

# Function to get embeddings using OpenAI
def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    return openai.Embedding.create(input=[text], model=model)["data"][0]["embedding"]

# Get embeddings for all FAQ questions
faq_embeddings = {q: get_embedding(q) for q in faq_data}
faq_questions = list(faq_data.keys())
faq_embedding_list = [faq_embeddings[q] for q in faq_questions]
faq_embedding_array = np.array(faq_embedding_list)

def find_best_answer(user_question):
    user_embedding = get_embedding(user_question)
    similarity_scores = cosine_similarity([user_embedding], faq_embedding_array)[0]
    best_match_index = np.argmax(similarity_scores)
    return faq_questions[best_match_index], faq_data[faq_questions[best_match_index]]

# Streamlit App
st.title("Gen Spark AI Courses FAQ Assistant")
st.write("Ask me anything about our AI courses!")

user_question = st.text_input("Your Question:")

if user_question:
    with st.spinner("Thinking..."):
        best_question, answer = find_best_answer(user_question)
        st.subheader("Best Matching Question:")
        st.write(best_question)
        st.subheader("Answer:")
        st.write(answer)
