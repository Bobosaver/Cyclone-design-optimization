import streamlit as st
import matplotlib.image as mpimg
from streamlit_extras.app_logo import add_logo

add_logo(r'合肥水泥院logo.png',height=60)
st.write("<p style='color: black; text-align:center;font-weight:bold;font-size:35px'>项目成果展示</p>",unsafe_allow_html=True)
st.write("<p style='color: black; text-indent:2em;font-weight:bold;font-size:22px;'>对仿真模型的降阶化处理以及后处理是实现数字孪生的\
         必要条件与手段，这个Web App介绍了本仿真中心进行的相关工作以及提供了部分参数化设计优化功能</p>",unsafe_allow_html=True)
st.write("<h5 style='color:#008B00 ;'>已开展内容一览：</h5>", unsafe_allow_html=True)

st.write("<p style='color: black; text-align:center;font-weight:bold;font-size:25px'>旋风筒参数拟合与优化</p>",unsafe_allow_html=True)
p1_col1, p1_col2, p1_col3 = st.columns(3)

with p1_col1:
    p1_img1 = mpimg.imread(r'./pages/images/Cyclone_Seperator_big2.jpg')
    st.image(p1_img1,caption='压降与流场')
with p1_col2:
    p1_img2 = mpimg.imread(r'./pages/images/收集率拟合曲线.jpg')
    st.image(p1_img2,caption='收集率拟合曲线')
with p1_col3:
    p1_img3 = mpimg.imread(r'./pages/images/响应面拟合.jpg')
    st.image(p1_img3,caption='拟合响应面')  

st.write("<p style='color: black; text-align:center;font-weight:bold;font-size:25px'>球磨机参数拟合与优化</p>",unsafe_allow_html=True)
p3_col1, p3_col2= st.columns(2)
with p3_col1:
    p3_img1 = mpimg.imread(r'.\pages\images\球磨机单变量预测.png')
    st.image(p3_img1,caption='球磨机单参数拟合曲线')
with p3_col2:
    p3_img2 = mpimg.imread(r'.\pages\images\球磨机多变量拟合面.png')
    st.image(p3_img2,caption='球磨机多参数拟合曲面')

st.write("<p style='color: black; text-align:center;font-weight:bold;font-size:25px'>分解炉参数拟合与优化</p>",unsafe_allow_html=True)
p3_col1, p3_col2= st.columns(2)
with p3_col1:
    p3_img1 = mpimg.imread(r'./pages/images/分解炉温度.png')
    st.image(p3_img1,caption='分解炉出口温度')
with p3_col2:
    p3_img2 = mpimg.imread(r'.\pages\images\氮氧化物排放率.png')
    st.image(p3_img2,caption='氮氧化物排放率',use_column_width=True)
