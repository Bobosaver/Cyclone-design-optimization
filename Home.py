import streamlit as st
import matplotlib.image as mpimg

#放置合肥水泥院LOGO
logo = mpimg.imread(r'Sinoma_ico.png',width=30)
st.image(logo,caption='')

#合肥水泥院简介
.shadowbox {
  width: 15em;
  border: 1px solid #333;
  box-shadow: 8px 8px 5px #444;
  padding: 8px 12px;
  background-image: linear-gradient(180deg, #fff, #ddd 40%, #ccc);
}



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


    
