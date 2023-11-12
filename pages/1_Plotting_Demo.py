import streamlit as st
tab1,tab2,tab3=st.tabs(['Trang chủ','Cà phê','Trà'])
with tab1:
  st.image('https://hcm.fstorage.vn/images/2023/11/banner-canvas-20231108021333.jpg')
  col1,col2=st.columns(2)
  with col1:
    st.image('https://phuclong.com.vn/uploads/post/20649d183ca5f1-bannertrangchu.jpg')
  with col2:
    st.text('Từ những mầm trà, chúng tôi tạo ra niềm đam m ê')
with tab2:
  st.image("https://phuclong.com.vn/upload/files/2/tra%20cafe/Dam%20vi%20ca%20phe%203''.jpg")
  st.header('HẠT CÀ PHÊ PHÚC LONG')
  tab21,tab22,tab23,tab24=st.tabs(['Đậm vị hạt cà phê rang xay','Hương vị tinh tế','Hương vị mạnh mẽ','Cà phê mùi'])