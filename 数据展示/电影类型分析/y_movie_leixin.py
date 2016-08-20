#-*-coding:utf-8-*-

import numpy as np
import matplotlib.pyplot as plt


def pylot_show():
    count=[]
    leixing = []
    leixing_number={}
    with open("000000_0.txt", "r", encoding="utf-8") as fp:
        for line in fp.readlines():
            leixing_number[line.strip().split("\t")[0]] = int(line.strip().split("\t")[1])
            leixing.append(line.strip().split("\t")[0])
            count.append(int(line.strip().split("\t")[1]))

    y_pos = np.arange(len(leixing))  # 定义y轴坐标数
    plt.barh(y_pos, count, align='center', alpha=0.4)  # alpha图表的填充不透明度(0~1)之间
    plt.yticks(y_pos, leixing)  # 在y轴上做分类名的标记

    for count, y_pos in zip(count, y_pos):
        # 分类个数在图中显示的位置，就是那些数字在柱状图尾部显示的数字
        plt.text(count, y_pos, count, horizontalalignment='center', verticalalignment='center', weight='bold')
    plt.ylim(+40.0, -1.0)  # 可视化范围，相当于规定y轴范围
    plt.title(u'剧情类型统计')  # 图表的标题
    plt.ylabel(u'剧情类型')  # 图表y轴的标记
    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(u'出现次数')  # 图表x轴的标记
    plt.savefig('Y_leixing.png')  # 保存图片
    plt.show()

pylot_show()
