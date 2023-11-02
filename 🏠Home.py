import streamlit as st
import matplotlib.image as mpimg
from streamlit_extras.app_logo import add_logo

#放置合肥水泥院LOGO
logo = mpimg.imread(r'Sinoma_ico.png')
st.image(logo,caption='')

add_logo(r'合肥水泥院logo.png',height=60)

st.write("")
st.write("")
st.write("")

#合肥水泥院简介
st.write("<p style='color: black; text-indent:2em; line-height:35px;font-weight:bold;font-size:22px '>合肥水泥研究设计院有限公司是世界财富500强企业——中国建材集\
         团的全资子公司，是中国建材行业重点科研院所和甲级设计单位。合肥院主要从事以水泥为特色的无机非金属材料领域技\
         术和装备的研发、生产和销售，以及提供配套技术服务，在水泥生产技术的研发应用、装备制造和技术服务领域享有盛誉。</p>",unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")

#一些装备的介绍
col1, col2, col3 = st.columns(3)
with col1:
    img1 = mpimg.imread(r'./pages/images/合肥水泥院介绍.jpg')
    st.image(img1,caption='')
    st.write("<p style='color: #00008B; text-align:center;font-weight:bold;font-size:20px'>公司平台</p>",unsafe_allow_html=True)
    st.write("<span style='color: black; text-align:center'>创新和运营“双元驱动”，“四位一体”生态链，\
    实现科研——工程——科研互相反哺的良性循环；拥有多个国家、省市级科研平台,多项技术成果被列入国家重大科技\
    成果推广计划。2020年被评为国家技术创新示范企业，2022年在国资委“双百行动”专项考核中被评为标杆企业。</span>",unsafe_allow_html=True)


with col2:
    img2 = mpimg.imread(r'./pages/images/HFGG系列辊压机.jpg')
    st.image(img2,caption='')
    st.write("<p style='color: #00008B; text-align:center;font-weight:bold;font-size:20px'>HFGG系列高性能辊压机</p>",unsafe_allow_html=True)
    st.write("<span style='color: black; text-align:center'>HFCG系列辊压机是我国拥有自主知识产权的水\
    泥生产关键主机装备，荣获国家科学技术进步二等奖两项、全国首批制造业单项冠军、中国工业大奖提名奖、中国名\
    牌产品等。截止2021年12月，全球在用量超过1800台套，广泛应用于建材、矿山等大宗物料粉碎领域，主要技术经济\
    指标达到国际先进水平。</span>",unsafe_allow_html=True)

with col3:
    img3 = mpimg.imread(r'./pages/images/HP强涡流型多风道煤粉燃烧器.png')
    st.image(img3,caption='') 
    st.write("<p style='color: #00008B; text-align:center;font-weight:bold;font-size:20px'>HP煤粉燃烧器</p>",unsafe_allow_html=True)
    st.write("<span style='color: black; text-align:center'>高性能的燃烧器是回转窑煅烧水泥熟料的关键设\
    备之一，中建材（合肥）热工装备科技有限公司在消化吸收国外先进技术的基础上，结合我国燃料条件研制开发的HP型\
    多通道燃烧器，是国内唯一通过中国建材联合会鉴定的新一代高性能燃烧器</span>",unsafe_allow_html=True)


    
