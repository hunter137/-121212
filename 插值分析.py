import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
plt.rcParams['font.sans-serif'] = ['simhei']
plt.rcParams['axes.unicode_minus'] = False
data=pd.read_excel(open('洗发水销售数据.xlsx', 'rb'), sheet_name='Sheet1')
x= data['自变量']
y= data['因变量']
print('光滑因子默认为0.1 如需修改请查看源码')
print('默认内插法分析')
print('请输入要插值自变量的起始值:')
input1=input(int())
print('请输入要插值自变量的中止值：')
input2=input(int())
print('请输入要插入点的个数：')
input3=input(int())
print('请输入图表标题：')
input4=input(str())
print('请输入自变量名称：')
input5=input(str())
print('请输入因变量名称：')
input6=input(str())

xnew = np.linspace(int(input1),int(input2),int(input3))
fSpl1 = UnivariateSpline(x, y, s=0)
y1 = fSpl1(xnew)
fSpl2 = UnivariateSpline(x, y)
y2 = fSpl2(xnew)
fSpl2.set_smoothing_factor(0.1)
y3 = fSpl2(xnew)
print("拟合后最终结果为：%s"%y3)

fig, ax = plt.subplots(figsize=(8,6))
plt.plot(x, y,'s',markersize=15,
         markerfacecolor="black",label="真实值")
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.plot(xnew, y3, 'b--', label="插值结果",ms=10)
plt.xlabel(str(input5),size=14)
plt.ylabel(str(input6),size =14)
ax.set_title(str(input4))
plt.legend(loc="best")
with open('插值结果.txt',"w+",encoding='utf-8') as fp:
    fp.write(str(y3))
plt.show()