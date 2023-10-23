import streamlit as st
st.title('帮助')

#选择参考文档
op_func =['旋风分离器响应面拟合','旋风分离器收集率曲线拟合及收集效率计算','旋风分离器总收集效率计算']
choose_func = st.radio('您对以下哪个功能有所疑问？',op_func)

if choose_func == op_func[0]:
    op_ques =['响应面拟合算法','上传数据样本格式']
    choose_ques = st.radio('您想了解的哪部分内容？',op_func)
    if choose_ques == op_ques[0]:
    
  
  
