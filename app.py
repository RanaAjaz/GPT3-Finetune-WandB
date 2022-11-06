
import streamlit as st
import os
import openai

openai.api_key = ""

api_key = st.sidebar.text_input("APIkey", type="password")
os.environ["OPENAI_API_KEY"] = api_key
openai.api_key = api_key

st.header("GPT-3 Intent Classifier")
question  = st.text_area("Enter Text/Question")
button = st.button("Generate Reply")

def generate_reply(review):
    response = openai.Completion.create(
    model="davinci:ft-personal-2022-10-30-06-01-45",
    prompt=f"This is an intent classification bot. Identify the intent of the give question.\n\nQuestion:{question}\n\nIntent:",
    temperature=0,
    max_tokens=5,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    st.write(response)
    return response.choices[0].text

if button and question:
    with st.spinner("Generating Reply..."):
        reply = generate_reply(question)
    st.write(reply)