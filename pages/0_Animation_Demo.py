import streamlit as st
import numpy as np

message = st.chat_message("A")
message.write("Hello human:alien:")
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
    