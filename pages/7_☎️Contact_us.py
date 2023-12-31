import streamlit as st
import matplotlib.image as mpimg
from streamlit_extras.app_logo import add_logo

add_logo(r'合肥水泥院logo.png',height=60)

st.write("<p style='color: black; text-align:center;font-weight:bold;font-size:35px'>联系我们</p>",unsafe_allow_html=True)
st.write("<span style='font-size: 20px;color: Black;'>这是一个刚刚开始搭建的Web app，页面和功能都很简陋，因此更需要您的宝贵意见：</span>", unsafe_allow_html=True)
st.write("<span style='font-size: 18px;color: #191970;'>1.希望加入的功能</span>", unsafe_allow_html=True)
st.write("<span style='font-size: 18px;color: #191970;'>2.页面布局的任何调整</span>", unsafe_allow_html=True)
st.write("<span style='font-size: 18px;color: #191970;'>3.现有Bug的优化</span>", unsafe_allow_html=True)

img = mpimg.imread(r'./pages/images/OK.jpg')
st.image(img,caption='')
st.write("<span style='font-size: 20px;color: #191970;'>如果您有任何意见或是使用的困扰，不妨致电或者是微信联系我。</span>", unsafe_allow_html=True)
st.write("<span style='font-size: 19px;color: green;'>微信：</span>","<span style='font-size: 18px;color: black;'>ytf2810192</span>",unsafe_allow_html=True)
st.write("<span style='font-size: 19px;color: green;'>电话：</span>","<span style='font-size: 18px;color: black;'>17756262359</span>",unsafe_allow_html=True)


