import streamlit as st

message = st.chat_message("A")
message.write("Hello human :alien:")

namelist = ['thư', 'anh', 'hương', 'tú', 'thanh', 'vy', 'phương','uyên','cindy', 'mary', 'tatyana', 'katy', 'alina', 'ivy', 'julie','elena']

prompt = st.chat_input("Nhập tên", key='name')

if prompt is not None:
    prompt_lower = prompt.lower()
    if prompt_lower in namelist:
        message = st.chat_message("A")
        message.write(f"TRỜI ƠI HÍ LU {prompt.upper()} ")
        message = st.chat_message("A")
        message.write('MÌNH CHU CÀ MO BẠN')
    else:
        message = st.chat_message("A")
        message.write("Bạn là ai z huheo")
        message = st.chat_message("A")
        message.write(f"Chào bạn {prompt} cuti nho")
else:
    message = st.chat_message("A")
    message.write("Please enter a name.")