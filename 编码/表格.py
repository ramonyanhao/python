import pandas as pd
from pyecharts.charts import Bar
import numpy as np
from pyecharts.charts import Pie
#饼图Pie
pie = Pie()
goodsA=["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
goodsB=["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
shopsA=[5, 20, 36, 10, 75, 90]
shopsB=[5, 20, 36, 10, 75, 90]
list1=list(zip(goodsA,shopsA))
list1.extend(list(zip(goodsB,shopsB)))
print(list1)
#饼图用的数据格式是[(key1,value1),(key2,value2)]，所以先使用 zip函数将二者进行组合
pie.add("饼图实例",list1)
pie.render('pie.html')
#柱线图Bar
bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
bar.add_yaxis("商家B", [5, 20, 36, 10, 75, 90])
bar.add_yaxis("商家C", [5, 20, 36, 10, 75, 90])
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
print(bar)
bar.render('bar.html')
#词云图WordCloud
from pyecharts.charts import WordCloud
name =['Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications', 'Chick Fil A', 'Planet Fitness',
       'Pitch Perfect', 'Express', 'Home', 'Johnny Depp', 'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark',
       'Farrah Abraham', 'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break','我是延浩']
value =[10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112, 965, 847, 582, 555, 550, 462, 366, 360, 282, 273, 265,9999]
list2=list(zip(name,value))
print(list2)
wordcloud =WordCloud()
wordcloud.add("云词图", list2, word_size_range=[20, 100])
wordcloud.render('wordcloud.html')
'''
pyecharts包含的图表
　　Bar（柱状图/条形图） 
　　Bar3D（3D 柱状图） 
　　Boxplot（箱形图） 
　　EffectScatter（带有涟漪特效动画的散点图） 
　　Funnel（漏斗图） 
　　Gauge（仪表盘） 
　　Geo（地理坐标系） 
　　Graph（关系图） 
　　HeatMap（热力图） 
　　Kline（K线图） 
　　Line（折线/面积图） 
　　Line3D（3D 折线图） 
　　Liquid（水球图） 
　　Map（地图） 
　　Parallel（平行坐标系） 
　　Pie（饼图） 
　　Polar（极坐标系） 
　　Radar（雷达图） 
　　Sankey（桑基图） 
　　Scatter（散点图） 
　　Scatter3D（3D 散点图） 
　　ThemeRiver（主题河流图） 
　　WordCloud（词云图）

　　用户自定义

　　Grid 类：并行显示多张图 
　　Overlap 类：结合不同类型图表叠加画在同张图上 
　　Page 类：同一网页按顺序展示多图 
　　Timeline 类：提供时间线轮播多张图
'''