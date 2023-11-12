import time
import streamlit as st
import numpy as np
time.sleep(0.5)
message = st.chat_message("A")
message.write("Hello human ")
st.toast('meow', icon='👽')
namelist = ['thư', 'anh', 'hương', 'tú', 'thanh', 'vy', 'phương','uyên','cindy', 'mary', 'tatyana', 'katy', 'alina', 'ivy', 'julie','elena']

prompt = st.chat_input("Nhập tên nếu b iu dy dăn", key='name')
if prompt is not None:
    prompt_lower = prompt.lower()
    if prompt_lower in namelist:
        time.sleep(0.5)
        message = st.chat_message("A")
        message.write(f"TRỜI ƠI HÍ LU {prompt.upper()} ")
        time.sleep(0.5)
        message = st.chat_message("A")
        message.write('MÌNH CHU CÀ MO BẠN')
        st.toast('con chó sủa meo meow chào bạn', icon='😍')
        time.sleep(0.5)
        st.link_button('tặng bạn một vid ho như cháy','https://www.youtube.com/watch?v=Q2BzgdPKq_U')
    else:
        time.sleep(0.5)
        message = st.chat_message("A")
        message.write("Bạn là ai z huheo")
        time.sleep(0.5)
        message = st.chat_message("A")
        message.write(f"Mà hoi chào bạn {prompt} cuti nho")
        time.sleep(0.5)
        st.link_button('tặng bạn một vid cringe','https://www.youtube.com/watch?v=YQHsXMglC9A')
        st.toast('gâu gâu', icon='🏋️‍♀️')

else:
    time.sleep(0.5)
    message = st.chat_message("A")
    message.write("Nhập tên hộ tui cái")