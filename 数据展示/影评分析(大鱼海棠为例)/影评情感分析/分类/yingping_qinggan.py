#encoding:utf-8

from numpy import *

#构造文档列表和标签列表
def loadDataSet():
    wordList = []
    typeList = [0,1,2,3,4]#0~4代表5种类型
    for i in range(0,5):
        lineList = []
        with open("%s.txt" % i,"r") as fp:
            for line in fp.readlines():
                lineList.append(line.strip())
        wordList.append(lineList)
    return wordList,typeList

#求所有文档的并集
def createBingjiList(wordList):
    bingjiList = set([])        #调用set方法创建一个空集
    for doc in wordList:
        bingjiList = bingjiList | set(doc)   #创建两个集合并集
    return list(bingjiList)

#如果一个文档在该词库中，那么出现该单词的位置由0变成1
def setOfWords(bingjiList,inputList):
    returnList = [0] * len(bingjiList)          #创建以一个所有元素都为0的向量
    for word in inputList:
        if word in bingjiList:
            returnList[bingjiList.index(word)] =1
    return returnList

'''
def writeList(wordList,bingjiList):
    fp1 = open("word.txt","a")
    for i in range(len(wordList)):
        fp1.write(str(wordList[i]))
        fp1.write("\n")
    fp1.close()
        
    fp2 = open("bingji.txt","a")
    for i in range(len(bingjiList)):
        fp2.write(str(bingjiList[i]))
        fp2.write("\n")
    fp2.close()
'''
#朴素贝叶斯分类器训练集
def trainBayes(trainMatrix,trainTag):
    pA = []      #任意文档属于0-4类别的概率
    for i in range(0,5):
        pA.append(trainTag.count(i)/float(len(trainTag)))
    numTrainDocs= len(trainMatrix)    #文档矩阵的长度
    numWords = len(trainMatrix[0])     #文档矩阵第一行的单词个数
    #初始化每个标签对应的矩阵，总数，避免某一个概率为0最后乘积为0，so初始化分子为1分母为2
    p0Num = ones(numWords);p0Denom = 2.0
    p1Num = ones(numWords);p1Denom = 2.0
    p2Num = ones(numWords);p2Denom = 2.0
    p3Num = ones(numWords);p3Denom = 2.0
    p4Num = ones(numWords);p4Denom = 2.0
    for i in range(numTrainDocs):
        if trainTag[i] == 0:
            p0Num +=trainMatrix[i];p0Denom +=sum(trainMatrix[i])
        elif trainTag[i] == 1:
            p1Num +=trainMatrix[i];p1Denom +=sum(trainMatrix[i])
        elif trainTag[i] == 2:
             p2Num +=trainMatrix[i];p2Denom +=sum(trainMatrix[i])
        elif trainTag[i] == 3:
            p3Num +=trainMatrix[i];p3Denom +=sum(trainMatrix[i])
        elif trainTag[i] == 4:
            p4Num +=trainMatrix[i];p4Denom +=sum(trainMatrix[i])
    pV = []
    pV0 = log(p0Num/p0Denom);pV.append(pV0)  
    pV1 = log(p1Num/p1Denom);pV.append(pV1)
    pV2 = log(p2Num/p2Denom);pV.append(pV2)
    pV3 = log(p3Num/p3Denom);pV.append(pV3)
    pV4 = log(p4Num/p4Denom);pV.append(pV4)

    return pA,pV

#朴素贝叶斯分类函数
def classifyBayes(testDoc,pV,pA):
    p0 = sum(testDoc * pV[0]) + log(pA[0])
    p1 = sum(testDoc * pV[1]) + log(pA[1])
    p2 = sum(testDoc * pV[2]) + log(pA[2])
    p3 = sum(testDoc * pV[3]) + log(pA[3])
    p4 = sum(testDoc * pV[4]) + log(pA[4])
    listValue = [p0,p1,p2,p3,p4]
    return listValue.index(max(listValue))

#从文本中得到数据
def getDoc():
    import jieba
    print ("准备中......\n请稍等......")
    fp = open("test.txt",'r')
    wordList = []
    strDocList = fp.readlines()
    for strDoc in strDocList:
        full_seg = jieba.cut(strDoc.strip(),cut_all = True)
        for word in full_seg:
            if len(word)>0:  #去除标点符号
                if ord(word[0])<127:
                    wordList.append(word.lower())
                else:
                   wordList.append(word)
    return wordList

def testingBayes():
    wordList,typeList = loadDataSet()
    bingjiList = createBingjiList(wordList)
    trainMat = []   #创建一个空的列表
    for lineDoc in wordList:
        trainMat.append(setOfWords(bingjiList,lineDoc))#使用词向量来填充trainMat列表
    pA,pV = trainBayes(trainMat,typeList)
    testDoc = getDoc()      #从文本中得到数据
    thisList = array(setOfWords(bingjiList,testDoc))
    return classifyBayes(thisList,pV,pA)

if __name__=="__main__":
    type = ['很差','较差','还行','推荐','力荐']
    classifiedNum = testingBayes()
    print ("the text is classified as:",str(type[classifiedNum]))
