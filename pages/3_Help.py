import streamlit as st
import matplotlib.image as mpimg

st.title('帮助')
#选择参考文档
op_func =['***旋风分离器响应面拟合***','**旋风分离器收集率曲线拟合及收集效率计算**','***旋风分离器总收集效率计算***']
choose_func = st.radio('您对以下哪个功能有所疑问？',op_func,index=None)

if choose_func == op_func[0]:
    op_ques =['***响应面拟合算法***','***上传数据样本格式***']
    choose_ques = st.radio('您想了解哪部分内容？',op_ques,index=None)
    if choose_ques == op_ques[0]:
        st.write("<p style='color: red; text-indent:2em'>当前主要的响应面拟合算法包括多项式插值算法和基于大\
        数据样本的机器学习算法。本Web app可选择采用三种拟合算法：</p>",unsafe_allow_html=True)
        op_algorithm = ['***三次卷积插值算法***','***三次样条插值算法***','***梯度提升算法***','***算法的选择与比较***']
        choose_algorithm = st.radio('您想了解哪种算法的详细情况？',op_algorithm,index=None)
        if choose_algorithm == op_algorithm[0]:
            img = mpimg.imread(r'./Help/三次卷积插值.png')
            st.image(img,caption='')
        if choose_algorithm == op_algorithm[1]:
            img = mpimg.imread(r'./Help/三次样条插值.png')
            st.image(img,caption='')
        if choose_algorithm == op_algorithm[2]:
            st.write("<p style='color: red; text-indent:2em'>当前主要的响应面拟合算法包括多项式插值算法和基于大\
            数据样本的机器学习算法。本Web app可选择采用三种拟合算法：</p>",unsafe_allow_html=True)            
        if choose_algorithm == op_algorithm[3]:
            
        
            
            
            
        
    
  
  
