import streamlit as st
import matplotlib.image as mpimg

st.write("<span style='font-size: 20px;color: Black;'>这是一个刚刚开始搭建的Web app,因此页面和功能都很简陋，因此更需要您的宝贵意见：</span>", unsafe_allow_html=True)
st.write("<span style='font-size: 18px;color: #191970;'>1.希望加入的功能</span>", unsafe_allow_html=True)
st.write("<span style='font-size: 18px;color: #191970;'>2.页面布局的任何调整</span>", unsafe_allow_html=True)
st.write("<span style='font-size: 18px;color: #191970;'>3.现有Bug的优化</span>", unsafe_allow_html=True)
col1, col2, col3 = st.columns()
with col2:
    img = mpimg.imread(r'./pages/images/OK.jpg')
    st.image(img,caption='',width=30)



