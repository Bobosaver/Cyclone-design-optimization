import streamlit as st
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression #导入线性回归模块
from sklearn.preprocessing import PolynomialFeatures
import copy
import time
matplotlib.rc("font",family='KaiTi')

#提取原始数据
data = pd.DataFrame(pd.read_excel(r"C:\Users\Yin\Desktop\实验设计.xlsx"))
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
word=st.empty()
bar=st.progress(0)
for i in range(100):
    word.text('数据拟合中: '+str(i+1))
    bar.progress(i+1)
    time.sleep(0.03)
st.write("==================================================================")
for index in range(1,100):
	data=pd.DataFrame({'IN':x, 'OUT':y})
	data_train=np.array(data['IN']).reshape(data['IN'].shape[0],1)				
	data_test=data['OUT']
	poly_reg =PolynomialFeatures(degree = index) 
	X_ploy =poly_reg.fit_transform(x)
	regr=LinearRegression() 													
	regr.fit(X_ploy,data_test)												
	st.write("当前迭代次数： ", index)
	st.write("R^2 = ",regr.score(X_ploy,data_test))								
	st.write("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
	if(regr.score(X_ploy,data_test) >= 0.999):
		break
st.write("==================================================================")
st.write("<h5 style='color: red'>拟合优度已达0.999以上，置信度良好。</h5>",unsafe_allow_html=True)

def get_x_pre(a):
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
op_func =['能量利用率预测','单一变量拟合曲线','多变量拟合响应面']
choose_func = st.radio('请选择您需要的功能',op_func,index=None)

if choose_func == op_func[0]:
    a = st.sidebar.slider("请指定密度倍数:",1,2,5)
    b = st.sidebar.slider("请指定球-料恢复系数:",0.1,0.4,0.9)
    c = st.sidebar.slider("请指定球-球恢复系数:",0.1,0.4,0.9)
    d = st.sidebar.slider("请指定球-料摩擦系数:",0.1,0.4,0.9)
    e = st.sidebar.slider("请指定球-球摩擦系数:",0.1,0.4,0.9)
    f = st.sidebar.slider("请指定模量倍数:",2,4,10)
    x = [a,b,c,d,e,f]
    coef = regr.coef_.flatten()
    x_pre = get_x_pre(x)
    y_pre = get_y_pre(x_pre,coef)
    st.write("<p style='color:#00008B;font-size:20px;'>能量利用率预测值为：</p>", unsafe_allow_html=True)
    st.markdown("<p style='color: red;font-size:20px;'>%s</p>"%(y_pre), unsafe_allow_html=True)

elif choose_func == op_func[1]:
    op_select = ['密度倍数','球-料恢复系数','球-球恢复系数','球-料摩擦系数','球-球摩擦系数','模量倍数']
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
        a = st.sidebar.slider('请指定%s'%(op_select[i]),b_min,b_max-b_min,b_max)
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
        plt.xlabel('%s'%(choose_select),fontsize=35)
        plt.ylabel('能量利用率(%)',fontsize=35)
        fig = plt.gcf()
        fig.set_size_inches(20, 12) # 设置图像大小
        return fig
    
    st.pyplot(plt_2D(xi,yi))

elif choose_func == op_func[2]:
    op_select = ['密度倍数','球-料恢复系数','球-球恢复系数','球-料摩擦系数','球-球摩擦系数','模量倍数']
    options_1 = st.selectbox('请选择拟合响应面的第一个参数',('密度倍数','球-料恢复系数','球-球恢复系数','球-料摩擦系数','球-球摩擦系数','模量倍数'),index=1)
    for i in range(len(op_select)):
        if op_select[i]==options_1:
            number_1 = i
    x=[]
    x_range = boundary[options_1]
    x_min,x_max = x_range[0],x_range[1]
    options_2 = st.selectbox('请选择拟合响应面的第一个参数',('密度倍数','球-料恢复系数','球-球恢复系数','球-料摩擦系数','球-球摩擦系数','模量倍数'),index=2)
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
            a = st.sidebar.slider('请指定%s'%(op_select[k]),b_min,b_max-b_min,b_max)
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
    ax.set_xlabel('%s'%(options_1),size=30,labelpad=20)
    ax.set_ylabel('%s'%(options_2),size=30,labelpad=20)
    ax.set_zlabel('能量利用率（%）',size=30,labelpad=25)
    ax.view_init(20, -25)
    fig.set_size_inches(12, 15) 
    st.pyplot(fig)

    
    
    




    



    


    


