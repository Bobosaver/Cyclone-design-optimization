import streamlit as st
import matplotlib.image as mpimg 

st.header('本项目简要介绍')
st.write("<h3 style='color: black;'>这个Web App针对旋风筒结构关键参数及主要边界条件进行参数化仿真</h3>",unsafe_allow_html=True)
st.write("<h3 style='color: black;'>并对结果进行后处理，以选定最优参数</h3>", unsafe_allow_html=True)
st.write("<h3 style='color: blue;'>目前具有以下功能：</h3>", unsafe_allow_html=True)
st.write("<h5 style='color: red;'>1.响应面拟合(风速/粒径—收集率）</h5>", unsafe_allow_html=True)
st.write("<h5 style='color: red;'>2.粒径—收集率曲线拟合(基于双R曲线的高精度拟合）</h5>", unsafe_allow_html=True)
st.write("<h5 style='color: red;'>3.总收集效率计算</h5>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
current_dir = os.path.dirname(os.path.abspath(__file__))
st.write(current_dir)
with col1:
    img1 = mpimg.imread(r'cyclone_Seperator_big2.jpg')
    st.image(img1,caption='压降与流场')

with col2:
    img2 = mpimg.imread(r'收集率拟合曲线.jpg')
    st.image(img2,caption='收集率拟合曲线')

with col3:
    img3 = mpimg.imread(r'响应面拟合.jpg')
    st.image(img3,caption='拟合响应面')  
