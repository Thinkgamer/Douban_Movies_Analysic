#-*-coding:utf-8-*-

#定义一个字典存放result
result_dic = {}
with open("result.txt","r",encoding="utf-8") as fp :
    for line in fp.readlines():
        if len(line.strip().split(",")[0]) > 1:
            result_dic[line.strip().split(",")[0]]=int(line.strip().split(",")[1])

#字典排序
sort_result_dic = sorted(result_dic.items(),key=lambda dic:dic[1],reverse = True)
for word,num in sort_result_dic:
    #print(word,"\t" , num)
    with open("sort_result.txt","a") as fpw:
        fpw.write(word+"\t"+str(num)+"\n")

print("OK !!!")
