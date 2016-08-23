#-*-coding:utf-8-*-

fpw = open("result.txt","a",encoding="utf-8")

with open("part-00000","r",encoding="utf-8") as fp1:
    for line in fp1.readlines():
        fpw.write(line[1:-2]+ "\n")

with open("part-00001","r",encoding="utf-8") as fp1:
    for line in fp1.readlines():
        fpw.write(line[1:-2]+ "\n")

fpw.close()
print("succeed")
