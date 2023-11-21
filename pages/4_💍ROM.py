import streamlit as st
import matplotlib.image as mpimg 
import time

st.write("<p style='color: black; text-align:center;font-weight:bold;font-size:35px'>旋风分离器ROM降阶模型</p>",unsafe_allow_html=True)
st.link_button('进一步了解'+':orange[ROM降阶模型]','https://zhuanlan.zhihu.com/p/566332825',use_container_width=True)
if st.button('点击进行'+':orange[可交互式ROM降阶模型]',use_container_width=True):
   st.write('<iframe src="http://4166e44h40.imdo.co",height="450",width="700"></iframe>',unsafe_allow_html=True)
