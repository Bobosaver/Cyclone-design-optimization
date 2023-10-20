import streamlit as st
import matplotlib.image as mpimg

st.write("<h1 style='color: black; text-align:center;'>旋风分离器拟合响应面项目介绍</h3>",unsafe_allow_html=True)
st.write("<h3 style='color: black; text-indent:2em'>这个Web App针对旋风筒结构关键参数及主要边界条件进行参数化仿真，并对结果进行后处理，以选定最优参数</h3>",unsafe_allow_html=True)
st.write("<h3 style='color: black;'>目前具有以下功能：</h3>", unsafe_allow_html=True)
st.write("<h5 style='color: red;'>1.响应面拟合(风速/粒径—收集率）</h5>", unsafe_allow_html=True)
st.write("<h5 style='color: red;'>2.粒径—收集率曲线拟合(基于双R曲线的高精度拟合）</h5>", unsafe_allow_html=True)
st.write("<h5 style='color: red;'>3.总收集效率计算</h5>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    img1 = mpimg.imread(r'./pages/images/Cyclone_Seperator_big2.jpg')
    st.image(img1,caption='压降与流场')

with col2:
    img2 = mpimg.imread(r'./pages/images/收集率拟合曲线.jpg')
    st.image(img2,caption='收集率拟合曲线')

with col3:
    img3 = mpimg.imread(r'./pages/images/响应面拟合.jpg')
    st.image(img3,caption='拟合响应面')  
