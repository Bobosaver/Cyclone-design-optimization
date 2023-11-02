import streamlit as st
import matplotlib.image as mpimg
from streamlit_extras.app_logo import add_logo
       
add_logo(r'合肥水泥院logo.png',height=60)

st.write("<p style='color: black; text-align:center;font-weight:bold;font-size:35px'>仿真中心现有成果</p>",unsafe_allow_html=True)

#现有的成果
outcome = ['柱钉造型优化','V型选粉机造型优化','辊压机优化']
my_bar=st.empty()
choose_oc = my_bar.radio('请选择您想查看的工作成果',outcome,index=None)

if choose_oc == outcome[0]:
    my_bar.empty()
    st.write("sss")
    if st.button("Return"):
        st.cache()
