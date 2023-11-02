import streamlit as st
import matplotlib.image as mpimg
from streamlit_extras.app_logo import add_logo

add_logo(r'合肥水泥院logo.png',height=60)
st.title('帮助')
op_main = [':violet[理论与算法简析]',':green[使用指南]']
choose_main = st.radio('您想了解哪部分内容？',op_main,index=None)

if choose_main == op_main[0]:
    op_ques =['***响应面拟合算法***','***ROM降阶模型***','***多参量寻优***']
    choose_ques = st.radio('您想了解哪部分理论？',op_ques,index=None)
    if choose_ques == op_ques[0]:
        op_algorithm = ['***三次卷积插值算法***','***三次样条插值算法***','***多元多项式拟合算法***','***梯度提升算法***','***算法的选择与比较***']
        choose_algorithm = st.radio('您想了解哪种算法的详细情况？',op_algorithm,index=None)
        if choose_algorithm == op_algorithm[0]:
            img = mpimg.imread(r'./Help/三次卷积插值.png')
            st.image(img,caption='')
            st.link_button('进一步了解'+':orange[三次卷积插值算法]','https://www.cnblogs.com/Pyrokine/p/15174298.html',use_container_width=True)
        if choose_algorithm == op_algorithm[1]:
            img = mpimg.imread(r'./Help/三次样条插值.png')
            st.image(img,caption='')
            st.link_button('进一步了解'+':orange[三次样条插值算法]','https://www.cnblogs.com/Pyrokine/p/15174298.html',use_container_width=True)
        if choose_algorithm == op_algorithm[2]:
            st.write("<p style='color: black; text-indent:2em'>在python—sklearn库中，对于多元多项式的的拟合仍然基于线性最小二\
            乘法原理，但是对数据进行了多项式特征构建和标准化处理。多项式特征构建通过增加自变量的次数，将数据映射到高维空间，实\
            现非线性数据转化为线性，以便使用核函数在低维空间中计算。</p>",unsafe_allow_html=True)
            img = mpimg.imread(r'./Help/非线性多项式回归1.png')
            st.image(img,caption='')
            img = mpimg.imread(r'./Help/非线性多项式回归2.png')
            st.image(img,caption='')
            st.link_button('进一步了解'+':orange[多项式拟合算法]','https://blog.csdn.net/HHG20171226/article/details/102749751',use_container_width=True)
        if choose_algorithm == op_algorithm[3]:
            st.write('')
            st.write('')
            st.write("<p style='color: black; text-indent:2em'>梯度提升算法指将多个简单模型合并到单个复合模型中的一种方式。\
            简单模型（即弱学习模型）一次添加一个，而梯度提升算法则可以在原复合模型上不断累加，持续强化，同时保持模型中的现有树\
            不变。随模型的不断组合强化，完整的最终模型可以实现更强大的预测能力，能够对连续值进行较好的预测。梯度提升算法将当前预\
            测和已知正确目标值之间的差值称为残差，并将对残差的提升回归训练为一个弱模型，将变量映射到该残差。弱模型预测的此残差将\
            添加到现有模型输入中，并进行反复迭代以改进整体模型预测。</p>",unsafe_allow_html=True) 
            img = mpimg.imread(r'./Help/梯度提升算法.jpg')
            st.image(img,caption='')
            st.link_button('进一步了解'+':orange[梯度提升算法]','https://blog.csdn.net/weixin_39910711/article/details/124450141',use_container_width=True)
        if choose_algorithm == op_algorithm[4]:
            st.write("<p style='color: black; text-indent:2em'>我们基于2参数的77组样本数据进行了三种算法的响应面拟合，在这个\
            样本量级下，多项式函数插值拟合算法得到的响应面更为平滑、分辨率更高，与验证点间的误差也会更小。如果样本数量进一步提高至\
            千个以上，基于机器学习的算法则可能具有更高的置信度。</p>",unsafe_allow_html=True) 
            img = mpimg.imread(r'./Help/拟合算法比较.png')
            st.image(img,caption='')
        
    if choose_ques == op_ques[1]:
        st.write("<p style='color: black; text-indent:2em'>数字孪生旨在充分利用物理模型、传感器更新、运行历史等数据，集成多学\
                 科、多物理量、多尺度、多概率的大样本仿真计算，在虚拟空间中完成映射，从而反映相对应的实体装备的全生命周期过程\
                。传统仿真手段计算时间长、数据时效性低，难以满足数字孪生实时交互的需求，而基于降低原始系统系数矩阵的阶次的Redu\
                ced Order Models，也就是ROM降阶模型方法，在可接受精度下能极大程度降低计算速度，为数字孪生提供了有效支撑。目前R\
                OM模型已被应用在结构仿真、系统电路模拟和流体力学仿真等多个领域，成为数字孪生领域内的主要实现手段。</p>",unsafe_allow_html=True)
        st.write("<p style='color: black; text-indent:2em'>下面以旋风分离器为例，展示了基于其Fluent模型进行的ROM降阶模型搭建过程。\
                由于当前Ansys内置的ROM功能仍不完善，针对颗粒收集率等关键指标尚不能实现降阶，因此该部分指标采用Python进行数据的后处\
                理，采用响应面拟合功能进行关键指标的预测。</p>",unsafe_allow_html=True)
        img = mpimg.imread(r'./Help/旋风分离器ROM降阶模型的搭建.jpg')
        st.image(img,caption='')
        st.link_button('视频教程：'+':blue[如何生成ROM降阶模型]','https://www.ansys.com/zh-cn/blog/how-to-build-reduced-order-model-cfd-simulations',use_container_width=True)
        st.link_button('进一步了解'+':orange[ROM降阶模型]','https://zhuanlan.zhihu.com/p/566332825',use_container_width=True)
    
    if choose_ques == op_ques[2]:
        st.write("<p style='color: black; text-indent:2em'>多参数寻优本质上是一个求解多元函数在有约束条件下的极值问题，目前有\
                 相当多的算法可以胜任，包括单纯形法(Nelder-Mead)、拟牛顿法(BFGS)、连续最小二乘法(SLSQP)等，本Web直接调用\
                 scipy.optimize.minimize库函数进行求解。</p>",unsafe_allow_html=True)
        code = '''scipy.optimize.minimize(fun, x0, args=(), method=None,
            jac=None, hess=None, hessp=None, bounds=None, constraints=(), 
            tol=None, callback=None, options=None)'''
        st.code(code,language='python')
        img = mpimg.imread(r'./Help/scipy.optimize.minimize函数用法.png')
        st.image(img,caption='')
        st.link_button('进一步了解'+':orange[scipy.minimize]'+'函数库','https://zhuanlan.zhihu.com/p/566332825',use_container_width=True)

            
        
            
            
            
        
    
  
  
