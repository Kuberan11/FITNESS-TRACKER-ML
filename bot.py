import streamlit as st
import pandas as pd
import google.generativeai as genai

st.title("Chatbot with Fitness Dataset")

uploaded_file = r"C:\Users\kuber\Downloads\Fitness_data.csv"  # Path to your uploaded dataset
try:
    data = pd.read_csv(uploaded_file)
except Exception as e:
    st.error(f"Error loading the dataset: {e}")
    data = None

api_key = 'AIzaSyDFT0YvA1S9lpklX7xFJWyuqJrrdpcT9vw'  # Replace with your valid API key
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def generate_content(prompt):
    try:
        response = model.generate_content([prompt])
        return response.text if response else "Error: No response received."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# User interaction
user_question = st.text_input("Ask me anything:")

if st.button("Get Answer"):
    if user_question:
        # Corrected line: Remove the context variable
        full_prompt = f"Question: {user_question}" 
        answer = generate_content(full_prompt)
        st.write(f"Answer: {answer}")
    else:
        st.write("Please enter a question to get an answer.")
