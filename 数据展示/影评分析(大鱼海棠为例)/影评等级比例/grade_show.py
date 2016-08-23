#-*-coding:utf-8-*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

grade = []
number = []

with open("yingping_grade.txt","r") as fp:
    for line in fp.readlines():
        print(line.strip().split("\t")[0],line.strip().split("\t")[1],"\n")
        grade.append(line.strip().split("\t")[0])
        number.append(line.strip().split("\t")[1])

mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = [u'SimHei']

plt.pie(number, labels=grade ,autopct="%d%%",explode = [0,0,.2, 0, 0])
plt.title("影评等级比例图")

plt.savefig("grade.png")
plt.show()
