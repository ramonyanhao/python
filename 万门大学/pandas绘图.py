import matplotlib.pyplot as plt
import numpy as np
import os

x = np.linspace(0, 10, 100)  # 随机生成0到10之间100个数字
plt.plot(x, np.sin(x))  # 绘制图形，使用100个随机数，然后通过正弦函数绘制曲线
plt.show()  # 显示出一条曲线图
plt.plot(x, np.cos(x))  # 两次绘图，通过余弦
plt.plot(x, np.sin(x))  # 两次绘图，通过正弦
plt.show()  # 显示出两条曲线图
# 保存matplotlib图形
fig = plt.figure()  # 生成一个画布fig
plt.plot(x, np.sin(x), '--')  # 然后使用虚线绘图
plt.show()  # 显示绘制的图形
fig.savefig(os.getcwd()+os.path.sep+'fig.png')  # 把生成的虚线图保存为fig.png文件
# 把图拆分开
plt.subplot(2, 1, 1)  # 把一个图形分开为2行1列，第一个图形
plt.plot(x, np.cos(x))
plt.subplot(2, 1, 2)  # 把一个图形分开为2行1列，第二个图形
plt.plot(x, np.sin(x))
plt.show()
plt.plot(x, np.sin(x), 'o', color='red')  # 使用圆点来绘图,可以控制颜色
plt.show()
# 给图形添加标签，用来表示曲线属于哪个属性
plt.plot(x, np.sin(x), '--', label='sin(x)')
plt.plot(x, np.cos(x), 'o', label='cos(x)')
plt.legend(loc=3)  # legend就是就是添加标签,loc=0标签的位置默认放在右上角，loc=3标签放在左下角,也可以使用loc='upper right'
'''
            ===============   =============
            Location String   Location Code
            ===============   =============
            'best'            0
            'upper right'     1
            'upper left'      2
            'lower left'      3
            'lower right'     4
            'right'           5
            'center left'     6
            'center right'    7
            'lower center'    8
            'upper center'    9
            'center'          10
            ===============   =============
'''
plt.show()  # 显示两条曲线图，右上角有一个标签
y = np.linspace(0, 10, 20)
plt.plot(y, np.sin(y), '-p', color='gray',
         markersize=10, linewidth=2,  # markersize是五边形的大小，linewidth是连接五边形的线的粗细
         markerfacecolor='white',  # markerfacecolor是五边形里面填充的颜色，这里为白色
         markeredgecolor='gray',  # markeredgecolor是五边形边框的颜色，这里为灰色
         markeredgewidth=4)  # markeredgewidth是定义五边形外框线条的粗细
plt.show()  # 定义一个五边形的曲线图
# matplotlib截图
plt.plot(x, np.sin(x))
plt.ylim(-0.5, 1.2)
plt.xlim(2, 8)
plt.show()  # xlim和ylim用来截取图中的一部分
# matplotlib绘制散点图
a = np.random.rand(100)  # 绘制散点图x轴的属性为0到1之间100个随机数
b = np.random.rand(100)  # 绘制散点图y轴的属性为0到1之间100个随机数
colors = np.random.rand(100)  # 绘制散点图散点的颜色为0到1之间100个随机数
size = 1000 * np.random.rand(100)  # 绘制散点图散点的大小为0到1000之间100个随机数
plt.scatter(a, b, s=size, c=colors, alpha=0.5)  # scatter绘制散点图,s表示图中散点的大小,c表示散点的颜色,alpha表示绘制颜色的深浅
plt.colorbar()  # 在图的右边绘制一条颜色说明
plt.show()
# plt.style.use('seaborn-whitegrid')  用来控制图形版面的样式,classic是经典样式
# plt的所有参数
'''
**Colors**
    =============    ===============================
    character        color
    =============    ===============================
    ``'b'``          blue
    ``'g'``          green
    ``'r'``          red
    ``'c'``          cyan
    ``'m'``          magenta
    ``'y'``          yellow
    ``'k'``          black
    ``'w'``          white
    =============    ===============================
**Line Styles**
    =============    ===============================
    character        description
    =============    ===============================
    ``'-'``          solid line style
    ``'--'``         dashed line style
    ``'-.'``         dash-dot line style
    ``':'``          dotted line style
    =============    ===============================
**Markers**
    =============    ===============================
    character        description
    =============    ===============================
    ``'.'``          point marker
    ``','``          pixel marker
    ``'o'``          circle marker
    ``'v'``          triangle_down marker
    ``'^'``          triangle_up marker
    ``'<'``          triangle_left marker
    ``'>'``          triangle_right marker
    ``'1'``          tri_down marker
    ``'2'``          tri_up marker
    ``'3'``          tri_left marker
    ``'4'``          tri_right marker
    ``'s'``          square marker
    ``'p'``          pentagon marker
    ``'*'``          star marker
    ``'h'``          hexagon1 marker
    ``'H'``          hexagon2 marker
    ``'+'``          plus marker
    ``'x'``          x marker
    ``'D'``          diamond marker
    ``'d'``          thin_diamond marker
    ``'|'``          vline marker
    ``'_'``          hline marker
    =============    ===============================
示例格式字符串:
'b' #带有默认形状的蓝色标记或“红色圆圈”
'-g' #绿色实线
'——' #虚线，使用默认颜色
'^k:' #由虚线连接的黑色三角形标记
'''
# 使用pandas绘图
import pandas as pd
df = pd.DataFrame(np.random.rand(100, 4).cumsum(0), columns=['A', 'B', 'C', 'D'])
print(df)  # 使用np生成100行4列范围是0到1之间随机数的二维数组，然后cumsum(0)表示把数组中的元素按照行进行累加，0就是axis=0，4列每列的别名是'A', 'B', 'C', 'D'
# 线型图
df.plot()  # pandas内置了plot绘图功能，生成4条线性图
plt.show()
df.A.plot()  # 只生成一条数据的线性图
plt.show()
df1 = pd.DataFrame(np.random.randint(10, 50, (3, 4)), columns=['A', 'B', 'C', 'D'], index=['one', 'two', 'three'])
print(df1)
# df1生成一个10到50之间的整数，有3行4列，列的别名是['A', 'B', 'C', 'D'],索引是['one', 'two', 'three'],pandas默认索引为数字，例如通过索引访问df.loc[:2]读取前两行的数据
# 柱状图
df1.plot.bar()  # 生成柱状图，还可以使用df1.plot(kind='bar')生成柱状图，效果是一样的，kind='bar'（垂直柱状图）或kind='barh'（水平柱状图）
plt.show()
df1.A.plot.bar()  # 只生成一条数据的柱状图
plt.show()
df1.plot(kind='bar', stacked=True)  # stacked把4列数据['A', 'B', 'C', 'D']累加为一个柱形图
plt.show()
# 直方图
df1.hist()
plt.show()
# df1.hist(column='A', figsize=(8, 5))  只取出A列数据，也可以这样使用df1.A.hist()绘制A列数据的直方图，figsize为图形的大小
# 密度图,需要用到第三方库scipy，所以要提前安装scipy，生成密度图
df.plot.kde()  # 等价df.plot(kind='kde')
plt.show()
