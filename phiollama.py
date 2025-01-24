# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 23:34:47 2025

@author: Kiran Adhav
"""
from phi.run.response import RunEvent, RunResponse
from phi.agent import Agent, RunResponse
from phi.model.ollama import Ollama
import streamlit as st

def as_stream(response):
  for chunk in response:
    if isinstance(chunk, RunResponse) and isinstance(chunk.content, str):
      if chunk.event == RunEvent.run_response:
        yield chunk.content

agent = Agent(
    model=Ollama(id="llama2")
)

st.title('Phidata With LLAMA2 API')

if "messages" not in st.session_state:
  st.session_state.messages = []

for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])
    
if prompt := st.chat_input("Search the topic u want"):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  with st.chat_message("assistant"):
    chunks = agent.run(prompt, stream=True)
    response = st.write_stream(as_stream(chunks))
  st.session_state.messages.append({"role": "assistant", "content": response})