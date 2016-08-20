#-*-coding:utf-8-*-

from matplotlib import style
import matplotlib.pyplot as plt

style.use("ggplot")
#加载数据
leixing_number = {}
leixing = []
number = []
with open("000000_0.txt" , "r",encoding="utf-8") as fp:
    for line in fp.readlines():
        leixing_number[line.strip().split("\t")[0]] = int(line.strip().split("\t")[1])
        leixing.append(line.strip().split("\t")[0])
        number.append(int(line.strip().split("\t")[1]))
fig, ax = plt.subplots()
rects1 = plt.bar(range(1,len(leixing)+1), number, width=0.8, alpha=0.2, color='g',align="center") #条形图

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2.0, 1.05*height,'%d'%int(height), ha='center', va='bottom')

autolabel(rects1)

plt.xlabel(u"类型名字",color='r')  #横坐标
plt.ylabel(u"对应的电影数目",color='r')     #纵坐标
plt.title(u"类型-数目 分布图")           #图片名字
plt.xticks(range(1,len(leixing)+1),leixing,fontsize=12)      #x轴加上类别名称
plt.xticks(fontsize=9)            #y坐标数字显示大小
plt.savefig(u'leixing.png')
plt.show()     #显示
