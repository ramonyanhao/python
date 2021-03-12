import pandas as pd
from pyecharts.charts import Pie
from pyecharts import options as opts
import xlwings as xw

app = xw.App(add_book=False)
book = xw.Book(r'D:\Python\表02_电脑清单(软硬件) .xlsb')
sheet = book.sheets('资产表')
while True:
    try:
        sheet1 = book.sheets.add('new')
    except ValueError:
        book.sheets['new'].delete()
    else:
        break

rexcel = pd.DataFrame(sheet.range('B12').expand().value,columns=['团队',None,None,'配置',None,None,None,None,None])

max_num = len(rexcel)
team_list = {}
config_list = {}
team_config = {}


for i in rexcel.团队[-rexcel.团队.duplicated()]:
    team_list[i] = 0

for k,v in team_list.items():
    for l in rexcel.团队:
        if k == l:
            team_list[k] += 1

    for m in rexcel.配置[-rexcel.配置.duplicated()]:
        config_list[m] = 0
        for n in rexcel.iloc:
            if n.配置 == m:
                config_list[m] += 1

for q in team_list.keys():
    for p in config_list.keys():
        if p == '高配' or p == '顶配':
            team_config[q + '_' + p] = 0



for s in rexcel.iloc:
    for a in team_config.keys():
        if s.团队 == a[:a.index('_')] and s.配置 == a[a.index('_')+1:]:
            team_config[a] += 1


totle_config = {}
for c,l in config_list.items():
    percent = '%'+ str('%.2f' %float(l / max_num * 100))
    totle_config[c] = percent

totle_team = {}
for c,l in team_list.items():
    percent = '%'+ str('%.2f' %float(l / max_num * 100))
    totle_team[c] = percent

totle_team_config = {}
for c,l in team_config.items():
    if l != 0:
        for x,y in config_list.items():
            if c[c.index('_')+1:] == x:
                percent = '%' + str('%.2f' % float(l / y * 100))
                totle_team_config[c] = percent



out_content = pd.DataFrame.from_dict(totle_team_config,orient='index',columns=['percent'])
out_content1 = pd.DataFrame.from_dict(totle_config,orient='index',columns=['percent1'])
sheet1.range('A1').value = out_content
sheet1.range('D1').value = out_content1
book.save()

pie = Pie()

for k in list(team_config.keys()):
    if team_config[k] == 0:
        del team_config[k]


teama = team_config.keys()
teamb = team_config.values()
teamc = list(zip(teama,teamb))

pie.add('团队配置比例',teamc)

pie.set_global_opts(
    legend_opts=opts.LegendOpts(is_show=False))

pie.set_series_opts(
            label_opts=opts.LabelOpts(formatter="{b}: {c} ({d}%)"),
            tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        ))


pie.render('团队配置比例.html')