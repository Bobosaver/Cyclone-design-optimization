import streamlit as st
import matplotlib.image as mpimg

#放置合肥水泥院LOGO
logo = mpimg.imread(r'Sinoma_ico.png')
st.image(logo,caption='')

#一些装备的介绍
col1, col2, col3 = st.columns(3)
with col1:
    img1 = mpimg.imread(r'./pages/images/合肥水泥院介绍.jpg')
    st.image(img1,caption='')

with col2:
    img2 = mpimg.imread(r'./pages/images/HFGG系列辊压机.jpg')
    st.image(img2,caption='')

with col3:
    img3 = mpimg.imread(r'./pages/images/HP强涡流型多风道煤粉燃烧器.png')
    st.image(img3,caption='')  


    
