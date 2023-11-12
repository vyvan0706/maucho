import streamlit as st
import numpy as np

message = st.chat_message("A")
message.write("Hello human:alien:")
namelist=['thư','anh','hương','tú','thanh','vy','phương']
prompt = st.chat_input("Nhập tên")
if prompt in namelist
    st.write(f"Chào bạn cuti: {prompt}")
else: 
    st.write(f"Bạn là ai z huheo")
    
    