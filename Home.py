import streamlit as st
import matplotlib.image as mpimg

#放置合肥水泥院LOGO
logo = mpimg.imread(r'Sinoma_ico.png')
st.image(logo,caption='')

#合肥水泥院简介
st.write("<span style='color: black; text-indent:2em'>合肥水泥研究设计院有限公司是世界财富500强企业——中国建材集\
         团的全资子公司，是中国建材行业重点科研院所和甲级设计单位。合肥院主要从事以水泥为特色的无机非金属材料领域技\
         术和装备的研发、生产和销售，以及提供配套技术服务，在水泥生产技术的研发应用、装备制造和技术服务领域享有盛誉。</span>",unsafe_allow_html=True)



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


    
