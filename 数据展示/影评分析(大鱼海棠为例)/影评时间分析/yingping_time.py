#-*-coding:utf-8-*-

from matplotlib import  style
import matplotlib.pyplot as plt
style.use("ggplot")

fig, ax = plt.subplots()

#画图6.30-7.30影评数目走势
def show_near_yp_data(near_yp_data):
    yp_data = []  # 存放日期
    number = []  # 存放数目
    for ypd,nb in near_yp_data:
        yp_data.append(ypd % 20160700)
        number.append(nb)
    rects_near= plt.plot(range(1, len(yp_data) + 1), number, alpha=0.2, color="g")  # 条形图

    plt.xlabel(u"日期", color='r')  # 横坐标
    plt.ylabel(u"影评数目", color='r')  # 纵坐标
    plt.title(u"2016年7月份大鱼海棠影评数量走势")  # 图片名字
    plt.xticks(range(1, len(yp_data) + 1), yp_data,fontsize=10)  # x轴加上类别名称
    plt.yticks(fontsize=10)  # y坐标数字显示大小
    plt.savefig(u'monthzoushi.png')
    plt.show()  # 显示

if __name__=="__main__":
    # 加载数据
    yingping_of_data = {}
    with open("yingping_time.txt", "r") as fp_r:
        for line in fp_r.readlines():
            if int(line.strip().split("\t")[0]) <=20160731 and int(line.strip().split("\t")[0]) >20160700 :
                yingping_of_data[int(line.strip().split("\t")[0])] = int(line.strip().split("\t")[1])
    near_yp_data = {}  # 0630-0730影评的数量变化
    near_yp_data = sorted(yingping_of_data.items(), key=lambda dic: dic[0], reverse=False)
    show_near_yp_data(near_yp_data)
