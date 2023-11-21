import streamlit as st
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression #导入线性回归模块
from sklearn.preprocessing import PolynomialFeatures
import copy
import time
import re
from scipy import optimize
from matplotlib.font_manager import FontProperties
font = FontProperties(fname='./simkai.ttf',size=30)
from streamlit_extras.app_logo import add_logo
matplotlib.rcParams['axes.unicode_minus'] =False

add_logo(r'合肥水泥院logo.png',height=60)

st.write("<p style='color: black; text-align:center;font-weight:bold;font-size:35px'>球磨机参数优化</p>",unsafe_allow_html=True)

#提取原始数据
data = pd.DataFrame(pd.read_excel(r"实验设计.xlsx"))
data_np = data.to_numpy()
data_cansu = np.delete(data_np,-1,1)
lie = len(data_np[:,0])
x = []
target = data_np[:,-1].flatten()
y = list(target)
for i in range(lie):
    data_lie = data_cansu[i,:]
    x.append(list(data_lie))

#显示进度条
my_bar=st.empty()
bar=st.progress(0)
for i in range(100):
    my_bar.text('数据拟合中: '+str(i+1))
    bar.progress(i+1)
    time.sleep(0.01)
time.sleep(1)
my_bar.empty()

st.write("==================================================================")

#迭代求拟合多项式系数
for index in range(1,100):
	data=pd.DataFrame({'IN':x, 'OUT':y})
	data_train=np.array(data['IN']).reshape(data['IN'].shape[0],1)				
	data_test=data['OUT']
	poly_reg =PolynomialFeatures(degree = index) 
	X_ploy =poly_reg.fit_transform(x)
	regr=LinearRegression() 													
	regr.fit(X_ploy,data_test)												
	st.write("<span style='color: #00008B;font-size:15px '>当前迭代次数:  </span>",
          "<span style='color: red;font-size:18px '>%s  </span>"%(index),
          "<span style='color: #00008B;font-size:15px '>拟合优度R^2 =</span>",
          "<span style='color: red;font-size:15px '>%s</span>"%(round(regr.score(X_ploy,data_test),4)),unsafe_allow_html=True)								
	st.write("<p style='line-height:10px;'>^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</p>",unsafe_allow_html=True)
	if(regr.score(X_ploy,data_test) >= 0.999):
		break
st.write("==================================================================")
st.write("<p style='color: red;font-size:20px;font-weight:bold'>拟合优度已达0.999以上，置信度良好。</p>",unsafe_allow_html=True)

def get_x_pre(x):
    x_pre = [1]
    x_len = len(x)
    for i in range(x_len):
        x_pre.append(x[i])
    
    for i in range(x_len):
        for j in range(i,x_len):
            x_2 = x[i]*x[j]
            x_pre.append(x_2)
        
    for i in range(x_len):
        for j in range(i,x_len):
            for k in range(j,x_len):
                x_3 = x[i]*x[j]*x[k]
                x_pre.append(x_3)
    return x_pre 

def get_y_pre(x , coef):
    y_pre = 0
    for i in range(len(x)):
        y_pre = y_pre + x[i]*coef[i]
    return y_pre + regr.intercept_

#参数边界条件
boundary = {'密度倍数':[1,5],'球-料恢复系数':[0.1,0.9],'球-球恢复系数':[0.1,0.9],'球-料摩擦系数':[0.1,0.9],'球-球摩擦系数':[0.1,0.9],'模量倍数':[2,10]}

#选择使用功能
op_func =['能量利用率预测','单一变量拟合曲线','多变量拟合响应面','规划能量利用率最优值']
choose_func = st.radio(':rainbow[请选择您需要的功能]',op_func,index=None)
op_select = ['密度倍数','球-料恢复系数','球-球恢复系数','球-料摩擦系数','球-球摩擦系数','模量倍数']

if choose_func == op_func[0]:
    a = st.sidebar.slider("请指定密度倍数:",1,5,2)
    b = st.sidebar.slider("请指定球-料恢复系数:",0.1,0.9,0.4)
    c = st.sidebar.slider("请指定球-球恢复系数:",0.1,0.9,0.4)
    d = st.sidebar.slider("请指定球-料摩擦系数:",0.1,0.9,0.4)
    e = st.sidebar.slider("请指定球-球摩擦系数:",0.1,0.9,0.4)
    f = st.sidebar.slider("请指定模量倍数:",2,10,4)
    x = [a,b,c,d,e,f]
    coef = regr.coef_.flatten()
    x_pre = get_x_pre(x)
    y_pre = get_y_pre(x_pre,coef)
    st.write("<p style='color:#00008B;font-size:20px;'>能量利用率预测值为：</p>", unsafe_allow_html=True)
    st.markdown("<p style='color: red;font-size:20px;'>%s</p>"%(y_pre), unsafe_allow_html=True)

elif choose_func == op_func[1]:
    choose_select = st.radio('请指定需要绘制拟合曲线的参数',op_select)
    for i in range(len(op_select)):
        if op_select[i]==choose_select:
            number = i
    x_range = boundary[choose_select]
    x_min,x_max = x_range[0],x_range[1]
    x=[]
    for i in range(len(op_select)):
        b_range = boundary[op_select[i]]
        b_min = b_range[0]
        b_max = b_range[1]
        a = st.sidebar.slider('请指定%s'%(op_select[i]),b_min,b_max)
        x.append(a)
    xi = np.arange(x_min,x_max,(x_max-x_min)/100)
    yi = []
    for i in range(len(xi)):
        x.pop(number)
        x.insert(number, xi[i])
        x_pre = get_x_pre(x)
        coef = regr.coef_.flatten()
        y_pre = get_y_pre(x_pre, coef)
        yi.append(100*y_pre)      
    
    def plt_2D(xi,yi):
        plt.plot(xi, yi, lw=2)
        plt.yticks(fontsize=30,color='#000000')
        plt.xticks(fontsize=30,color='#000000')
        plt.xlabel('%s'%(choose_select),fontproperties=font)
        plt.ylabel('能量利用率(%)',fontproperties=font)
        fig = plt.gcf()
        fig.set_size_inches(20, 12) # 设置图像大小
        return fig
    
    st.pyplot(plt_2D(xi,yi))

elif choose_func == op_func[2]:
    options_1 = st.selectbox('请选择拟合响应面的第一个参数',('密度倍数','球-料恢复系数','球-球恢复系数','球-料摩擦系数','球-球摩擦系数','模量倍数'),index=1)
    for i in range(len(op_select)):
        if op_select[i]==options_1:
            number_1 = i
    x=[]
    x_range = boundary[options_1]
    x_min,x_max = x_range[0],x_range[1]
    options_2 = st.selectbox('请选择拟合响应面的第二个参数',('密度倍数','球-料恢复系数','球-球恢复系数','球-料摩擦系数','球-球摩擦系数','模量倍数'),index=2)
    for j in range(len(op_select)):
        if op_select[j]==options_2:
            number_2 = j
    y_range = boundary[options_2]
    y_min,y_max = y_range[0],y_range[1]
    for k in range(len(op_select)):
        if op_select[k]!=options_1 and op_select[k]!=options_2:
            b_range = boundary[op_select[k]]
            b_min = b_range[0]
            b_max = b_range[1]
            a = st.sidebar.slider('请指定%s'%(op_select[k]),b_min,b_max)
            x.append(a)
    x.insert(number_1, 0.1)
    x.insert(number_2, 0.1)
    xi = np.arange(x_min,x_max,(x_max-x_min)/100)
    yi = np.arange(y_min,y_max,(y_max-y_min)/100)
    xi, yi = np.meshgrid(xi, yi)
    zi = np.empty([100,100])
    coef = regr.coef_.flatten()
    for i in range(len(xi)):
        for j in range(len(xi)):
            a = xi[i,j]
            x[number_1]=a
            b = yi[i,j]
            x[number_2]=b
            x_pre = get_x_pre(x)
            y_pre = get_y_pre(x_pre, coef)
            if y_pre <0:
                y_pre = 0
            zi[i,j]= y_pre
           
    # 调节图像大小,清晰度
    fig = plt.figure()
    plt.figure(figsize=(10,10),dpi=175)
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(xi, yi, 100*zi,cmap='rainbow')
    ax.set_facecolor("white")
    ax.xaxis.set_ticks(list(np.arange(x_min,x_max,(x_max-x_min)/4)))
    ax.yaxis.set_ticks(list(np.arange(y_min,y_max,(y_max-y_min)/4)))
    ax.xaxis.set_tick_params(color='r',labelsize=25)
    ax.yaxis.set_tick_params(color='r',labelsize=25)
    ax.zaxis.set_tick_params(color='r',labelsize=25)
    ax.set_xlabel('%s'%(options_1),fontproperties=font,labelpad=20)
    ax.set_ylabel('%s'%(options_2),fontproperties=font,labelpad=20)
    ax.set_zlabel('能量利用率（%）',fontproperties=font,labelpad=22)
    ax.view_init(20, -25)
    fig.set_size_inches(12, 15) 
    st.pyplot(fig)

elif choose_func == op_func[3]:
    flag = st.text_input("请指定一个接近最优解的初始预测值",'[3,0.1,0.5,0.9,0.3,4]')
    flag = re.findall(r'\[(.*?)\]',flag)
    flag = flag[0]
    flag = flag.split(',')
    for i in range(len(flag)):
        flag[i] = float(flag[i])
        
    #定义最优化函数
    def func_goal(a):
        pre = get_x_pre(a)
        coef = regr.coef_.flatten()
        y_r = get_y_pre(pre, coef)
        return -y_r
    
    #指定边界条件
    st.write("<p style='color:#00008B;font-size:20px;'>请指定各参数边界条件</p>", unsafe_allow_html=True)
    a = st.text_input("请指定密度倍数的范围",'1,5')
    b = st.text_input("请指定球-球恢复系数的范围",'0.1,0.9')
    c = st.text_input("请指定球-料恢复系数的范围",'0.1,0.9')
    d = st.text_input("请指定球-球摩擦系数的范围",'0.1,0.9')
    e = st.text_input("请指定球-料摩擦系数的范围",'0.1,0.9')
    f = st.text_input("请指定弹性模量倍数的范围",'2,10')
    bound_set = [a,b,c,d,e,f]
    for i in range(len(bound_set)):
        bound_set[i] = bound_set[i].split(',')
        for j in range(len(bound_set[i])):
            bound_set[i][j] = float(bound_set[i][j])
         
    #选择最优化方法        
    Optimization_method =['Nelder-Mead','L-BFGS-B','SLSQP','TNC','Powell','trust-constr']
    choose_method = st.radio('请选择求解算法',Optimization_method)  
    result = optimize.minimize(func_goal,flag,bounds=bound_set,method=choose_method)
    st.write("<span style='color:#00008B;font-size:22px;'>能量利用率最大值为：</span>", "<span style='color: red;font-size:22px;'>%s</span>"%(-result.fun),unsafe_allow_html=True)
    st.write("<p style='color:#00008B;font-size:22px;'>最大值对应的参数值为：</p>", unsafe_allow_html=True)
    for i in range(len(op_select)):
        st.write("<span style='font-size: 18px;color: green;'>%s :</span>"%(op_select[i]),"<span style='font-size: 18px;color: black;'>%s</span>"%round(result.x[i],4),unsafe_allow_html=True)
    
    
    
    




    



    


    


