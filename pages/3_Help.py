import streamlit as st
import matplotlib.image as mpimg

st.title('帮助')
#选择参考文档
op_func =['***旋风分离器响应面拟合***','***旋风分离器收集率曲线拟合及收集效率计算***','***旋风分离器总收集效率计算***']
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
            st.write('')
            st.write('')
            st.write("<p style='color: black; text-indent:2em'>梯度提升算法指将多个简单模型合并到单个复合模型中的一种方式。\
            简单模型（即弱学习模型）一次添加一个，而梯度提升算法则可以在原复合模型上不断累加，持续强化，同时保持模型中的现有树\
            不变。随模型的不断组合强化，完整的最终模型可以实现更强大的预测能力，能够对连续值进行较好的预测。梯度提升算法将当前预\
            测和已知正确目标值之间的差值称为残差，并将对残差的提升回归训练为一个弱模型，将变量映射到该残差。弱模型预测的此残差将\
            添加到现有模型输入中，并进行反复迭代以改进整体模型预测。</p>",unsafe_allow_html=True) 
            img = mpimg.imread(r'./Help/梯度提升算法.jpg')
            st.image(img,caption='')
        if choose_algorithm == op_algorithm[3]:
            st.write("<p style='color: black; text-indent:2em'>我们基于2参数的77组样本数据进行了三种算法的响应面拟合</p>",unsafe_allow_html=True) 
            img = mpimg.imread(r'./Help/拟合算法比较.png')
            st.image(img,caption='')



            
        
            
            
            
        
    
  
  
