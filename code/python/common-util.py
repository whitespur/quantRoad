import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import numpy as np
# import statsmodels
import talib

# 各种常用类库
# https://github.com/HuaRongSAO/talib-document  https://mrjbq7.github.io/ta-lib/
# talib
"""
TA-Lib广泛应用与交易软件，和金融市场数据进行技术分析。
Includes 150+ indicators such as ADX, MACD, RSI, Stochastic, Bollinger Bands, etc.
Candlestick pattern recognition
Open-source API for C/C++, Java, Perl, Python and 100% Managed .NET
包含了150多个指标,包括：ADX, MACD, RSI, Stochastic, Bollinger Bands, 等.
K线形态识别
完全开源，支持 C/C++, Java, Perl, Python and 100% Managed .NET

install :https://mrjbq7.github.io/ta-lib/install.html

pip install TA-Lib
brew install ta-lib
"""

# https://www.ricequant.com/community/topic/174/




# numpy

"""
http://www.runoob.com/numpy/numpy-tutorial.html
NumPy(Numerical Python) 是 Python 语言的一个扩展程序库，支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。
NumPy 是一个运行速度非常快的数学库，主要用于数组计算，包含：
一个强大的N维数组对象 ndarray
广播功能函数
整合 C/C++/Fortran 代码的工具
线性代数、傅里叶变换、随机数生成等功能

NumPy 通常与 SciPy（Scientific Python）和 Matplotlib（绘图库）一起使用， 这种组合广泛用于替代 MatLab，是一个强大的科学计算环境，有助于我们通过 Python 学习数据科学或者机器学习。

SciPy 是一个开源的 Python 算法库和数学工具包。

SciPy 包含的模块有最优化、线性代数、积分、插值、特殊函数、快速傅里叶变换、信号处理和图像处理、常微分方程求解和其他科学与工程中常用的计算。

Matplotlib 是 Python 编程语言及其数值数学扩展包 NumPy 的可视化操作界面。它为利用通用的图形用户界面工具包，如 Tkinter, wxPython, Qt 或 GTK+ 向应用程序嵌入式绘图提供了应用程序接口（API）。

http://codingpy.com/article/an-introduction-to-numpy/
"""

# 添加标题，坐标轴标记和图例
# x = np.linspace(0, 2 * np.pi, 50)
# plt.plot(x, np.sin(x), 'r-x', label='Sin(x)')
# plt.plot(x, np.cos(x), 'g-^', label='Cos(x)')
# plt.legend() # 展示图例
# plt.xlabel('Rads') # 给 x 轴添加标签
# plt.ylabel('Amplitude') # 给 y 轴添加标签
# plt.title('Sin and Cos Waves') # 添加图形标题
# plt.show()

x = np.arange(100)
close = np.random.random(100)
output = talib.SMA(close)

# print('x is {}'.format(x))
# print('close is {}'.format(close))
# print('output is {}'.format(output))
# plt.subplot(2, 1, 1) # （行，列，活跃区）
# plt.plot(x,close,'r',label='close')
#
# plt.subplot(2, 1, 2)
# plt.plot(x,output,'g',label='sma')

# SMA = talib.SMA(close)
# EMA = talib.EMA(close)
# WMA = talib.WMA(close)
# DEMA = talib.DEMA(close)
# TEMA = talib.TEMA(close)

upper, middle, lower = talib.BBANDS(close)

mom = talib.MOM(close, timeperiod=5)

plt.plot(x,close,'r',label='close')
plt.plot(x,upper,'g',label='upper')
plt.plot(x,middle,'b',label='middle')
plt.plot(x,lower,'y',label='lower')
plt.grid()

# plt.plot(x, SMA)
# plt.plot(x, EMA)
# plt.plot(x, WMA)
# plt.plot(x, DEMA)
# plt.plot(x, TEMA)


plt.legend()
plt.show()

# note that all ndarrays must be the same length!
inputs = {
    'open': np.random.random(100),
    'high': np.random.random(100),
    'low': np.random.random(100),
    'close': np.random.random(100),
    'volume': np.random.random(100)
}

sma1 = talib.SMA(inputs)




# matplotlib
"""
http://codingpy.com/article/a-quick-intro-to-matplotlib/
Matplotlib 是 Python 的一个绘图库。它包含了大量的工具，你可以使用这些工具创建各种图形，包括简单的散点图，正弦曲线，甚至是三维图形。Python 科学计算社区经常使用它完成数据可视化的工作。
颜色： 蓝色 - 'b' 绿色 - 'g' 红色 - 'r' 青色 - 'c' 品红 - 'm' 黄色 - 'y' 黑色 - 'k'（'b'代表蓝色，所以这里用黑色的最后一个字母） 白色 - 'w' 线： 直线 - '-' 虚线 - '--' 点线 - ':' 点划线 - '-.' 常用点标记 点 - '.' 像素 - ',' 圆 - 'o' 方形 - 's' 三角形 - '^'
"""

# pandas
"""
Python 是进行数据分析的绝佳语言，主要原因是以数据为中心的 Python 包的奇妙生态系统。Pandas 就是其中之一，它使得导入和分析数据更容易。
Pandas 以 NumPy 和 matplotlib 包为底层驱动，为您提供更方便的接口用来完成大多数数据分析和可视化工作。
https://www.jianshu.com/p/d9774cf1fea5
http://codingpy.com/article/use-pandas-for-data-analysis-one/
http://jupyter.org/install.html
jupyter notebook

"""

# statsmodels
"""
"""




