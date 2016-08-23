#-*-coding:utf-8-*-

def write():
    with open("new_50455678.txt","r",encoding="utf-8") as fp_r:
        for line in fp_r.readlines():
            if line.strip().split("\t")[5]!="这篇影评可能有剧透":
                import jieba    
                word_list = jieba.cut(line.strip().split("\t")[5][:-7])
                grade = line.strip().split("\t")[3]
                if grade=="很差":
                    with open("0.txt","a") as fpw1:
                        for word in word_list:
                            if len(word)>1:
                                fpw1.write(word+"\n")
                elif grade=="较差":
                    with open("1.txt","a") as fpw1:
                        for word in word_list:
                            if len(word)>1:
                                fpw1.write(word+"\n")
                elif grade=="还行":
                    with open("2.txt","a") as fpw1:
                        for word in word_list:
                            if len(word)>1:
                                fpw1.write(word+"\n")
                elif grade=="推荐":
                    with open("3.txt","a") as fpw1:
                        for word in word_list:
                            if len(word)>1:
                                fpw1.write(word+"\n")
                elif grade=="力荐":
                    with open("4.txt","a") as fpw1:
                        for word in word_list:
                            if len(word)>1:
                                try:
                                    int(word)-1
                                except:
                                    fpw1.write(word+"\n")

def sort():
    #对五个等级下的文件进行词频统计，利用出现频率最高的N个词作为评判标准
    for i in range(0,5):
        with open("%s.txt" % i,"r") as fp:
            word_dic = {}
            for line in fp.readlines():
                if line.strip() not in word_dic.keys():
                    word_dic[line.strip()]=1
                else:
                    word_dic[line.strip()] +=1
        #排序
        new_word_dic = sorted(word_dic.items(),key = lambda a:a[1],reverse=True)
        for k,w in new_word_dic:
            with open("result/%s.txt" % i,"a") as fpw:
                if w>1:
                    fpw.write(k + "\n")

if __name__=="__main__":

    #write()
    sort()
    print("succeed")
