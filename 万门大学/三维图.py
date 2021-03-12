from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


# 三维曲面图
def surface_plot():
    fig = plt.figure()  # 准备一个画布
    ax = plt.axes(projection='3d')
    x = np.arange(-5, 5, 0.25)    # 生成[-5,5]间隔0.25的数列，间隔越小，曲面越平滑
    y = np.arange(-5, 5, 0.25)
    x, y = np.meshgrid(x, y)  # 格点矩阵,原来的x行向量向下复制len(y)次，形成len(y)*len(x)的矩阵，即为新的x矩阵；原来的y列向量向右复制len(x)次，形成len(y)*len(x)的矩阵，即为新的y矩阵；新的x矩阵和新的y矩阵shape相同
    r = np.sqrt(x ** 2 + y ** 2)
    z = np.sin(r)

    surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm)  # cmap指color map

    # 自定义z轴
    ax.set_zlim(-1, 1)
    ax.zaxis.set_major_locator(LinearLocator(20))  # z轴网格线的疏密，刻度的疏密，20表示刻度的个数
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))  # 将z的value字符串转为float，保留2位小数

    # 设置坐标轴的label和标题
    ax.set_xlabel('x', size=15)
    ax.set_ylabel('y', size=15)
    ax.set_zlabel('z', size=15)
    ax.set_title("Surface plot", weight='bold', size=20)

    # 添加右侧的色卡条
    fig.colorbar(surf, shrink=0.6, aspect=8)  # shrink表示整体收缩比例，aspect仅对bar的宽度有影响，aspect值越大，bar越窄
    plt.show()


surface_plot()


# 三维的线图和散点图
def scatter_plot():
    ax = plt.axes(projection='3d')

    # 三维线的数据
    zline = np.linspace(0, 15, 1000)
    xline = np.sin(zline)
    yline = np.cos(zline)
    ax.plot3D(xline, yline, zline, 'gray')

    # 三维散点的数据
    zdata = 15 * np.random.random(100)
    xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
    ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
    ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')
    plt.show()


scatter_plot()


# 三维等高线图
def contour_plot():
    def f(x, y):
        return np.sin(np.sqrt(x ** 2 + y ** 2))

    x = np.linspace(-6, 6, 30)
    y = np.linspace(-6, 6, 30)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.contour3D(X, Y, Z, 50, cmap='binary')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    # 调整观察角度和方位角。这里将俯仰角设为60度，把方位角调整为35度
    ax.view_init(60, 35)
    plt.show()


contour_plot()

# 绘制莫比乌斯带
def mobius_plot():
    # 由于它是一条二维带，因此需要两个内在维度。theta维度取值范围是0～2pi，宽度维度w取值范围是-1～1
    theta = np.linspace(0, 2 * np.pi, 30)
    w = np.linspace(-0.25, 0.25, 8)
    w, theta = np.meshgrid(w, theta)
    phi = 0.5 * theta
    # x-y平面内的半径
    r = 1 + w * np.cos(phi)

    x = np.ravel(r * np.cos(theta))
    y = np.ravel(r * np.sin(theta))
    z = np.ravel(w * np.sin(phi))

    # 要画出莫比乌斯带，还必须保证三角部分是正确的。最好的方法是首先用基本参数化方法定义三角部分，然后用Matplotlib将
    # 这个三角剖分映射到莫比乌斯带的三维空间里
    from matplotlib.tri import Triangulation
    tri = Triangulation(np.ravel(w), np.ravel(theta))
    ax = plt.axes(projection='3d')
    ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap='viridis', linewidth=0.2)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)

    plt.show()


mobius_plot()
