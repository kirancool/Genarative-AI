from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import streamlit as st

api_key=""

llm_llama=ChatGroq(model="gemma2-9b-it",api_key=api_key)

st.title("Blog Post Generator")

def generate_response(topic:str):
    template=""" As experienced startup and venture capital writer, generate a 400 world blog post about{topic}
                 Your repoonse should be in this format:
                 First, print the blog post.
                 Then,sum the total number of words on it and print result like this: This post has X words. """
    prompt = PromptTemplate( input_variables=["topic"],template=template)
    query= prompt.format(topic=topic)
    response=llm_llama.invoke(query,max_tokens=2048)
    blog_text = response.text()
    return st.write(blog_text)

topic_text=st.text_input("Enter topic")
if st.button("Search"):
    if topic_text:
        generate_response(topic_text)
        