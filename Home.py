import streamlit as st
import matplotlib.image as mpimg

#放置合肥水泥院LOGO
logo = mpimg.imread(r'Sinoma_ico.png')
st.image(logo,caption='')

#合肥水泥院简介
st.write("<h5 style='color: black; text-indent:2em'>合肥水泥研究设计院有限公司是世界财富500强企业——中国建材集\
         团的全资子公司，是中国建材行业重点科研院所和甲级设计单位。合肥院主要从事以水泥为特色的无机非金属材料领域技\
         术和装备的研发、生产和销售，以及提供配套技术服务，在水泥生产技术的研发应用、装备制造和技术服务领域享有盛誉。</h5>",unsafe_allow_html=True)

#一些装备的介绍
col1, col2, col3 = st.columns(3)
with col1:
    img1 = mpimg.imread(r'./pages/images/合肥水泥院介绍.jpg')
    st.image(img1,caption='')
    st.write("<spna style='color: black; text-indent:2em'>合肥院坚持创新和运营“双元驱动”，打造科研、设计、装备智造、工程服务“四位一体”生态链，\
    有效实现了“科研提升装备，设计优化工程，效益反哺科研设计”的良性循环。目前，合肥院拥有国家级企业技术中心、省、市企业技术中心、工程技术中心、工业\
    设计中心和研发实验基地等科研平台，是国家高新技术企业，拥有一个博士后工作站，设有先进控制实验室和固废综合处置与资源化实验室；年均科研项目40项以上，\
    多项技术成果被列入国家重大科技成果推广计划。2020年被评为国家技术创新示范企业，2022年在国资委“双百行动”专项考核中被评为标杆企业。</span>",unsafe_allow_html=True)


with col2:
    img2 = mpimg.imread(r'./pages/images/HFGG系列辊压机.jpg')
    st.image(img2,caption='')

with col3:
    img3 = mpimg.imread(r'./pages/images/HP强涡流型多风道煤粉燃烧器.png')
    st.image(img3,caption='')  


    
