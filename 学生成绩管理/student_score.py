import xlrd
from tkinter import *
import tkinter.filedialog
from pyecharts import options as opts
from pyecharts.charts import Line
class sf(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)  # 相当于执行了self.root=Tk()
        self.grid()
        self.filenames=''
        self.lb = Label(self, text='')
        self.lb.grid()
    def select_file(self):
        self.filename = tkinter.filedialog.askopenfilenames()
        if len(self.filename) != 0:
            for i in range(0,len(self.filename)):
                self.filenames+=str(self.filename[i])+'\n'
            self.lb.config(text = "您选择的文件是："+self.filenames)
    def sure_file(self):
        self.btn1 = Button(self,text="选择文件",command=self.select_file)
        self.btn1.grid(row = 2, column = 1)
        self.btn = Button(self, text="确定", command=self.quit)
        self.btn.grid(row = 2, column = 2)
        self.mainloop()
        return self.filename
class read_file:
    def __init__(self,file):
        self.file=file
        self.data = xlrd.open_workbook(self.file)
        self.table = self.data.sheets()[0]
        self.chine_proficiency_list = []   # 语文优秀率
        self.math_proficiency_list = []  # 数学优秀率
        self.english_proficiency_list = []  # 英语优秀率
        self.phycics_proficiency_list = []  # 物理优秀率
        self.chemical_proficiency_list = [] # 化学优秀率
        self.tscore_proficiency_list = []  # 总分优秀率
        self.chine_pass_rate = []  # 语文及格率
        self.math_pass_rate = []
        self.english_pass_rate = []
        self.phycics_pass_rate = []
        self.chemical_pass_rate = []
        self.tscore_pass_rate = []
        self.chine_No_pass = []  # 不及格
        self.math_No_pass = []
        self.english_No_pass = []
        self.phycics_No_pass = []
        self.chemical_No_pass = []
        self.tscore_No_pass = []
        '''
        语数外满分120，物化满分150,及格率是满分60%,优秀率是满分80%
        '''
    def student_score(self):
        l=[]
        for i in range(self.table.nrows):
            l.append(self.table.row_values(i,0,13))
        l.pop(0)
        student_name=[k[0] for k in l]
        line = Line(init_opts=opts.InitOpts(width='1600px',height='800px'))
        line1 = Line(init_opts=opts.InitOpts(width='1600px',height='800px'))
        totle_score=['语文成绩','数学成绩','英语成绩','物理成绩','化学成绩','总成绩']
        totle_rank=['语文名次','数学名次','英语名次','物理名次','化学名次','班级名次']
        self.student_name = student_name
        self.chine_score = [k[1] for k in l]
        self.chine_class_rank = [k[2] for k in l]
        self.math_score = [k[3] for k in l]
        self.math_class_rank = [k[4] for k in l]
        self.english_score = [k[5] for k in l]
        self.english_class_rank = [k[6] for k in l]
        self.phycics_score = [k[7] for k in l]
        self.phycics_class_rank = [k[8] for k in l]
        self.chemical_score = [k[9] for k in l]
        self.chemical_class_rank = [k[10] for k in l]
        self.tscore = [k[11] for k in l]
        self.class_rank = [k[12] for k in l]
        self.say=input('请输入需要创建成绩对比图的学生姓名:')
        if self.say in student_name:
            sindex=student_name.index(self.say)
            line.add_xaxis(totle_score)
            line.add_yaxis(self.say+'成绩', [self.chine_score[sindex],self.math_score[sindex],self.english_score[sindex],
                                      self.phycics_score[sindex],self.chemical_score[sindex],self.tscore[sindex]
                                      ],is_smooth=True,areastyle_opts=opts.AreaStyleOpts(opacity=0.5)
                          )
            line1.add_xaxis(totle_rank)
            line1.add_yaxis(self.say+'名次',[self.chine_class_rank[sindex],self.math_class_rank[sindex],self.english_class_rank[sindex],
                                           self.phycics_class_rank[sindex],self.phycics_class_rank[sindex],self.chemical_class_rank[sindex]
                                           ],is_smooth=True,areastyle_opts=opts.AreaStyleOpts(opacity=0.5))
        else:
            print('请输入正确学生姓名')
        line.render(self.say+'成绩'+'.html')
        line1.render(self.say+'名次'+'.html')
    def proficiency(self):
        for i in self.chine_score[2:]:
            if float(i) >= 96:
                self.chine_proficiency_list.append(float(i))
            elif float(i) >= 72 and float(i) < 96:
                self.chine_pass_rate.append(float(i))
            else:
                self.chine_No_pass.append(float(i))
        for i in self.math_score[2:]:
            if float(i) >= 96:
                self.math_proficiency_list.append(float(i))
            elif float(i) >= 72 and float(i) < 96:
                self.math_pass_rate.append(float(i))
            else:
                self.math_No_pass.append(float(i))
        for i in self.english_score[2:]:
            if float(i) >= 96:
                self.english_proficiency_list.append(float(i))
            elif float(i) >= 72 and float(i) < 96:
                self.english_pass_rate.append(float(i))
            else:
                self.english_No_pass.append(float(i))
        for i in self.phycics_score[2:]:
            if float(i) >= 120:
                self.phycics_proficiency_list.append(float(i))
            elif float(i) >= 90 and float(i) < 120:
                self.phycics_pass_rate.append(float(i))
            else:
                self.phycics_No_pass.append(float(i))
        for i in self.chemical_score[2:]:
            if float(i) >= 120:
                self.chemical_proficiency_list.append(float(i))
            elif float(i) >= 90 and float(i) < 120:
                self.chemical_pass_rate.append(float(i))
            else:
                self.chemical_No_pass.append(float(i))
        for i in self.tscore[2:]:
            if float(i) >= 528:
                self.tscore_proficiency_list.append(float(i))
            elif float(i) >= 396 and float(i) < 528:
                self.tscore_pass_rate.append(float(i))
            else:
                self.tscore_No_pass.append(float(i))
        line2 = Line(init_opts=opts.InitOpts(width='1600px', height='800px'))
        totle_score = ['语文成绩', '数学成绩', '英语成绩', '物理成绩', '化学成绩', '总成绩']
        line2.add_xaxis(totle_score)
        line2.add_yaxis('成绩优秀率',[len(self.chine_proficiency_list),len(self.math_proficiency_list),len(self.english_proficiency_list),
                                 len(self.phycics_proficiency_list),len(self.chemical_proficiency_list),len(self.tscore_proficiency_list)
                                 ],is_smooth=True)
        line2.add_yaxis('成绩及格率',[len(self.chine_pass_rate),len(self.math_pass_rate),len(self.english_pass_rate),
                                 len(self.phycics_pass_rate),len(self.chemical_pass_rate),len(self.tscore_pass_rate),
                                 ],is_smooth=True)
        line2.add_yaxis('不及格率',[len(self.chine_No_pass),len(self.math_No_pass),len(self.english_No_pass),
                                len(self.phycics_No_pass),len(self.chemical_No_pass),len(self.tscore_No_pass)],
                                is_smooth=True)
        line2.render('班级成绩及格率统计'+'.html')
    def average_score(self):  # 平均分
        totle_average_score=['数学成绩平均分','语文成绩平均分','英语成绩平均分','物理成绩平均分','化学成绩平均分','班级总分平均分']
        math_average_score=round(sum(self.math_proficiency_list+self.math_pass_rate+self.math_No_pass)/45,2)
        chine_average_score=round(sum(self.chine_pass_rate+self.chine_proficiency_list+self.chine_No_pass)/45,2)
        english_average_score=round(sum(self.english_pass_rate+self.english_proficiency_list+self.english_No_pass)/45,2)
        phycics_average_score=round(sum(self.phycics_pass_rate+self.phycics_proficiency_list+self.phycics_No_pass)/45,2)
        chemical_average_score=round(sum(self.chemical_pass_rate+self.chemical_proficiency_list+self.chemical_No_pass)/45,2)
        tscore_average_score=round(sum(self.tscore_pass_rate+self.tscore_proficiency_list+self.tscore_No_pass)/45,2)
        line3=Line(init_opts=opts.InitOpts(width='1600px', height='800px'))
        line3.add_xaxis(totle_average_score)
        line3.add_yaxis('平均分',[chine_average_score,math_average_score,english_average_score,phycics_average_score,
                               chemical_average_score,tscore_average_score],is_smooth=True,areastyle_opts=opts.AreaStyleOpts(opacity=0.5))
        line3.render('班级平均分统计'+'.html')
for i in sf().sure_file():
    if i[-1:i.find('.')] == 'xlsx' or 'xls':
        rfile=read_file(i)
        rfile.student_score()
        rfile.proficiency()
        rfile.average_score()




