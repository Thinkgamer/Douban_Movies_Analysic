#-*-coding:utf8-*-

class OutPut(object):
    def __init__(self):
        pass
    #输出所有热门类别和对应的电影数目
    def output_category(self,categort_dic):
        with open("file_output/category.csv","a") as fp:
            for cate_name,cate_num in categort_dic.items():
                fp.write(cate_name + "," + cate_num + "\n")
        print("write category OK !")
    #输出所有电影的详情页面链接
    def output_all_movies_href(self,movies_links):
        with open("file_output/movies_links.csv",'a') as fp_links:
            for links in movies_links:
                fp_links.write(links+"\n")
        print("one tag movies links write OK !")
    #输出一部电影的具体信息
    def output_one_movie_message(self,movie_message,id):
        #将除了剧情介绍之外的信息写进一个csv文件
        with open("file_output/movie.csv","a") as fp_one:
            fp_one.write(id+","+movie_message["movie_name"]+","+
                         movie_message['movie_daoyan']+","+
                         movie_message["movie_bianju"]+"," +
                         movie_message["movie_leixing"]+"," +
                         movie_message["movie_zhuyan"]+"," +
                         movie_message["movie_showtime"]+"," +
                         movie_message["movie_pianchang"]+"," +
                         movie_message["movie_disnum"]+","+
                         movie_message["movie_disscore"] + "\n")
        #将剧情介绍写进一个文件
        try:
            with open("file_output/movie_summary.txt","a") as fp_su:
                fp_su.write(id+"\t" + movie_message["movie_summary"]+"\n")
        except:
            fp_su.write(id + "\n")
        print("One Movie Write OK !\n")

    #将短评写进文件
    def output_duanping(self,mid,comment_list):
        for comment in comment_list:
            with open("file_output/duanping/%s .txt" % mid,"a",encoding="utf-8") as fp:
                try:
                    fp.write(mid+"\t"+comment.replace("\n","")+"\n")
                except Exception as e:
                    print("写入电影短评异常：",e)
                    pass

    #将电影影评写入文件
    def output_yingping(self, mid, comment_list):
        for comment in comment_list:
            if len(comment)!=5:
                pass
            else:
                try:
                    with open("file_output/yingping/%s .txt" % mid, "a",encoding="utf-8") as fp:
                        fp.write(mid+"\t"+comment["title"]+"\t"+comment["user"]+"\t"+comment["grade"]+"\t" + comment["time"] + "\t"+comment["content"]+"\n")
                except Exception as e:
                    print("写入电影影评异常：", e)
                    pass