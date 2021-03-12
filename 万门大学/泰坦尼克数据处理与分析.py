import pandas as pd
import matplotlib.pyplot as plt

titantic = pd.read_csv('train.csv')
pd.set_option('display.width', None)  # 设置数据展示宽度，如果没有把display.width设置为None,则结果只能显示几列，其余的都用省略号展示
pd.set_option('display.max_rows', None)  # 设置最大行数展示
pd.set_option('display.max_columns', None)  # 设置最大列数展示
print(titantic.head())
print(titantic.describe())  # describe把所有数值类型的数据做统计
print()
print(titantic.isnull().sum())  # 统计None值个数,Age里有177个空值
# titantic.Age.fillna(0) 把所有年龄为空的值改为0，但是年龄改为0又不好，所以下面可以把所有年龄为空的地方改为年龄的中位数，中位数是按顺序排列的一组数据中居于中间位置的数
titantic.Age.fillna(titantic.Age.median(), inplace=True)  # inplace=True代表直接在titantic中修改，把Age为空值填充为中位数,不会返回新的Series
# 如果没有inplace则不会填充空值，而是返回一个新的series，下面这行代码就是把返回的新值赋值给titantic_age_None变量
# titantic_age_None = titantic.Age.fillna(titantic.Age.median())  把所有年龄为None值改为Age的中位数,此时Age的中位数是28
print(titantic.isnull().sum())  # Age里的空值被改为了28，所以Age中没有空值
print()
# 计算泰坦尼克生还率，从性别开始分析
fig = plt.figure()  # 使用画布的好处是不用一下生成好多图形，来不及查看,所有图形都绘制在一个画布上
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使plt可以显示中文字符
ax = plt.subplot(3, 3, 1)  # 将画布分为两行两列，目前在第一个位置绘图
print(titantic.Sex.value_counts())  # 统计男性有多少人，女性有多少人
survived = titantic[titantic.Survived == 1].Sex.value_counts()  # 统计生还者中男性有多少人，女性有多少人，[titantic.Survived == 1]代表生还
dead = titantic[titantic.Survived == 0].Sex.value_counts()  # 统计未生还者中男性有多少人，女性有多少人，[titantic.Survived == 0]代表未生还
# 一条数据是Series类型，两条数据就可以组成DataFrame类型。series：只是一个一维数据结构，它由index和value组成。dataframe：是一个二维结构，除了拥有index和value之外，还拥有column。
# dataframe由多个series组成，无论是行还是列，单独拆分出来都是一个series。
df = pd.DataFrame([survived, dead], index=['survived', 'dead'])  # index代表索引名，如果没有index,dataframe生成的二位组行名是sex
print(df)  # dataframe按行读取:df.loc['survivied'],按列读取:df.female
df.plot(ax=ax, title='男女生还人数柱状图', kind='bar')  # 绘制柱状图
df = df.T  # df.T作用是把行改为列，把列改为行
print(df)
ax1 = plt.subplot(3, 3, 2)  # 将画布分为两行两列，目前在第2个位置绘图
df.plot(ax=ax1, kind='bar', title='融合男女生还人数柱状图', stacked=True)  # 绘制柱状图,stacked把图中的两条柱状融合为一条
df['p_survived'] = df.survived / (df.survived + df.dead)  # 给df增加一列数据，以百分比计算男，女生还者比例
df['p_dead'] = df.dead / (df.survived + df.dead)  # 给df增加一列数据，以百分比计算男，女未生还者比例
print(df)
print(df[['p_survived', 'p_dead']])  # 从df中取出p_surivied和p_dead两列数据
ax2 = plt.subplot(3, 3, 3)
df[['p_survived', 'p_dead']].plot(ax=ax2, kind='bar', title='百分比男女生还率', stacked=True)  # 按照百分比绘制男女生还率,从图中可以看出女性生还率大于男性

# 从年龄开始分析生还率
survived = titantic[titantic.Survived == 1].Age
dead = titantic[titantic.Survived == 0].Age
df = pd.DataFrame([survived, dead], index=['survived', 'dead'])
df = df.T
ax3 = plt.subplot(3, 3, 4)
df.plot(ax=ax3, kind='hist', title='年龄生还率直方图', stacked=True, bins=30)  # 绘制直方图,中间很高的柱子是因为我们之前把所有年龄为空值都替换成中位数28
ax4 = plt.subplot(3, 3, 5)
df.plot(ax=ax4, kind='kde', title='年龄生还率密度图', xlim=(0, 80))  # 使用密度图看的更直观一些,xlim限定取值范围为从0岁到80岁
print(titantic.Age.describe())  # 查看年龄最小为0.42岁，最大年龄为80岁

# 根据年龄分类
age = 18
young = titantic[titantic.Age <= age]['Survived'].value_counts()  # 取列中的值用['Survived']和.Survived效果一样
old = titantic[titantic.Age > age].Survived.value_counts()  # 小于18代表未成年，大于18代表成年人
df = pd.DataFrame([young, old], index=['young', 'old'])  # index代表索引，每一行的名字
df.columns = ['dead', 'survived']  # 给列添加名字，因为在Survived列中0代表死亡,1代表存活，到这里把Survived改成了两列数据0和1，所以需要给列改名dead和survived
df['p_survived'] = df.survived / (df.survived + df.dead)  # 给df增加一列数据，以百分比计算生还者比例
df['p_dead'] = df.dead / (df.survived + df.dead)
print(df)
ax5 = plt.subplot(3, 3, 6)
df[['p_survived', 'p_dead']].plot(ax=ax5, kind='bar', title='年龄分类', stacked=True)  # 和上面计算男女比例一样，从图中明显看出young的生存比例明显高于old

# 根据票价计算生还率
survived = titantic[titantic.Survived == 1].Fare  # 生还者
dead = titantic[titantic.Survived == 0].Fare  # 未生还者
df = pd.DataFrame([survived, dead], index=['survived', 'dead'])
df = df.T
print(titantic[titantic.Fare.values == 0])  # 找出票价为0的所有乘客
ax6 = plt.subplot(3, 3, 7)
df.plot(ax=ax6, kind='kde', title='票价计算生还率', xlim=(0, 513))  # 票价从0到513，从图中可以看出票价越高生存率越高，票价为0时未生还者(dead)明显高于生还者(survived)

# 组合特征，根据年龄和票价查看生还率
ax7 = plt.subplot(3, 3, 8)  # 在一个figure(画布)里创建多个小图（Subplot），或者单独生成一个画布
# 未生还者
age = titantic[titantic.Survived == 0].Age
fare = titantic[titantic.Survived == 0].Fare
ax7.set_xlabel('age')  # 给ax7子图上设置x轴名称为age
ax7.set_ylabel('fare')  # 给ax7子图上设置y轴名称为fare
ax7.scatter(age, fare, s=20, alpha=0.5, edgecolors='gray')  # scatter绘制散点图
# 生还者
age = titantic[titantic.Survived == 1].Age
fare = titantic[titantic.Survived == 1].Fare
ax8 = plt.subplot(3, 3, 9)
ax8.set_xlabel('age')  # 给ax7子图上设置x轴名称为age
ax8.set_ylabel('fare')  # 给ax7子图上设置y轴名称为fare
ax8.scatter(age, fare, s=20, alpha=0.5, edgecolors='gray', c='red')
plt.show()  # 把所有子图绘制完成后通过plt.show()统一显示出来
fig.savefig('泰坦尼克号生还率统计图.jpg')  # 可以把画布保存为图片文件,由于最后的合成图不在fig画布上，它是单独分出来一个字画布，所以没有保存到文件中
# 现在把这两个组合成一个图形
ax = plt.subplot()
ax.set_xlabel('age')
ax.set_ylabel('fare')
age = titantic[titantic.Survived == 0].Age
fare = titantic[titantic.Survived == 0].Fare
ax.scatter(age, fare, s=20, alpha=0.3, edgecolors='gray')
age = titantic[titantic.Survived == 1].Age
fare = titantic[titantic.Survived == 1].Fare
ax.scatter(age, fare, s=20, alpha=0.3, edgecolors='gray', c='red')
plt.show()

