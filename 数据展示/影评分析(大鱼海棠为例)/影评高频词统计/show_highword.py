#-*-coding:utf-8-*-

from matplotlib import style
import matplotlib.pyplot as plt

style.use("ggplot")
#加载数据
word_number = {}
with open("sort_result.txt" , "r") as fp:
    for line in fp.readlines():
        word_number[line.strip().split("\t")[0]] = int(line.strip().split("\t")[1])
word = []
number = []
word_number = sorted(word_number.items(),key = lambda dic:dic[1],reverse=True) #字典排序
for name,num in word_number[:20]:   #得到对应类别电影数目最多的20个类别
    word.append(name)
    number.append(num)

fig, ax = plt.subplots()
# plt.plot(range(1,len(category)+1),number) #折线图
rects1 = plt.bar(range(1,len(word)+1), number, width=0.4, alpha=0.4, color='g',align="center") #条形图

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2.0, 1.05*height,'%d'%int(height), ha='center', va='bottom')

autolabel(rects1)

plt.xlabel(u"高频词",color='r')  #横坐标
plt.ylabel(u"数目",color='r')     #纵坐标
plt.title(u"top20高频词")           #图片名字
plt.xticks(range(1,len(word)+1),word,fontsize=8)      #x轴加上类别名称
plt.yticks(fontsize=10)            #y坐标数字显示大小
plt.savefig(u'top20highword.png')
plt.show()     #显示
