#-*-coding:utf-8-*-

from matplotlib import style
import matplotlib.pyplot as plt

style.use("ggplot")
#加载数据
category_number = {}
with open("category.csv" , "r") as fp:
    for line in fp.readlines():
        category_number[line.strip().split(",")[0]] = int(line.strip().split(",")[1])
category = []
number = []
category_number = sorted(category_number.items(),key = lambda dic:dic[1],reverse=True) #字典排序
for name,num in category_number[:10]:   #得到对应类别电影数目最多的10个类别
    category.append(name)
    number.append(num)

fig, ax = plt.subplots()
# plt.plot(range(1,len(category)+1),number) #折线图
rects1 = plt.bar(range(1,len(category)+1), number, width=0.4, alpha=0.2, color='g',align="center") #条形图

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2.0, 1.05*height,'%d'%int(height), ha='center', va='bottom')

autolabel(rects1)

plt.xlabel(u"类别名字",color='r')  #横坐标
plt.ylabel(u"对应的电影数目",color='r')     #纵坐标
plt.title(u"类别-数目 分布图")           #图片名字
plt.xticks(range(1,len(category)+1),category,fontsize=12)      #x轴加上类别名称
plt.yticks(fontsize=10)            #y坐标数字显示大小
plt.savefig(u'top10category.png')
plt.show()     #显示
