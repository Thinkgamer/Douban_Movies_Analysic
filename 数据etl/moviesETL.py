# -*-coding:utf-8-*-

#encoding="utf-8"  保证导入hive之后查询时不会出现中文乱码
fp_w = open("new_movies_load.csv","a",encoding="utf-8")

with open("movie.csv","r") as fp_r:
    for line in fp_r.readlines():
        movies=line.strip().split(",")

        s = ""
        #对上映时间进行处理
        try:
            year = int(movies[6].replace("/","-").split("-")[0])
        except:
            yesr = ""
        try:
            month = int(movies[6].replace("/","-").split("-")[1])
        except:
            month = ""
        movies[6] = str(year) + "," + str(month)
        for m in movies:
            s += m+","
        fp_w.write(s[:-1]+"\n")
    print("OK !!!")
    fp_w.close()
        
        
