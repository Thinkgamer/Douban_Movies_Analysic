#-*-coding:utf-8-*-
from bs4 import BeautifulSoup
class ParaseHtml(object):
    def __init__(self):
        self.category_dic = {}
    #解析豆瓣电影所有热门标签
    def parase_category(self,content):
        page = BeautifulSoup(content)   #得到格式化后的网页源代码
        table = page.find(class_="tagCol")   #定位到类型
        for cate_name_and_num in table.find_all("td"):  #获取所有的类别行
            cate_name = cate_name_and_num.get_text().split("(")[0]      #类别名字
            cate_num = cate_name_and_num.get_text().split("(")[1][:-1]   #该类别对应的电影数目
            if cate_name not in self.category_dic.keys():  #存放在字典中
                self.category_dic[cate_name] = cate_num
        return self.category_dic
    #得到该分类存在多少页，这里存在只有一页的情况，所以加一个异常处理
    def parase_pagenum(self,content):
        page = BeautifulSoup(content)
        try:
            page_num = page.find(class_="thispage")["data-total-page"]
        except:
            page_num=1
        return page_num
    #得到每页所有电影详情页面的链接
    def parase_page_all_movies(self,content,movies_link):
        page = BeautifulSoup(content)
        tag_div_pl2 = page.find_all(class_="pl2")  #定位到每个电影的div
        try:
            for tag_div_pl2_one in tag_div_pl2[:-1]:   #解析得到每部电影的详情链接
                href = tag_div_pl2_one.a.get('href')
                print("href:\t",href)
                movies_link.append(href)
        except Exception as e:
            print(e)
            pass
        return movies_link     #返回该页的电影详情链接列表
    #得到每部电影的数据
    def parase_one_movie_message(self,one_content):
        one_movie_message = {}   #定义一个字典用来存放一部电影的相关信息
        page = BeautifulSoup(one_content)
        #需要获取的属性包括 电影ID/电影名字/导演/编剧/类型/主演/上映时间/片长/剧情简介/评价人数/豆瓣评分
        try:
            title = page.find(property="v:itemreviewed").get_text()     #电影名字
        except:
            title = ""
        try:
            summary = page.find(property="v:summary").get_text()        #剧情简介
        except:
            summary = ""
        try:
            daoyan=page.find(rel="v:directedBy").get_text()                    #导演
        except:
            daoyan=""

        try:
            zhuyan = page.find(class_="actor").get_text().split(":")[1]  #主演
        except:
            zhuyan = ""
        if len(page.find_all(class_="attrs"))==3:
            bianju = page.find_all(class_='attrs')[1].get_text()  # 编剧
        elif len(page.find_all(class_="attrs"))==2:
            try:
                page.find(rel="v:directedBy")
                page.find(class_="actor")
                bianju = ""
            except:
                try:
                    page.find(rel="v:directedBy")
                    bianju = page.find_all(class_='attrs')[1].get_text()
                except:
                    bianju = page.find_all(class_='attrs')[0].get_text()
        else:  #attrs长度为1
            try:
                page.find(rel="v:directedBy")
                bianju = ""
            except:
                try:
                    page.find(class_="actor")
                    bianju = ""
                except:
                    bianju = page.find_all(class_='attrs')[0].get_text()

        try:
            leixing = ""                                          #类型
            leixing_all = page.find_all(property="v:genre")
            for lx in leixing_all:
                leixing += lx.get_text()+"/"
        except:
            leixing =""

        try:
            pianchang = page.find(property="v:runtime")['content']  # 片长
        except:  # 如果是剧集的形式
            pianchang = ""
        try:
            showtime = ""                                          #上映时间
            showtime_all = page.find_all(property="v:initialReleaseDate")
            for st in showtime_all:
                showtime+=st.get_text()+"/"
        except:
            showtime=""

        try:
            disnum = page.find(property="v:votes").get_text()      #评价人数
        except:
            disnum=""
        try:
            disscore = page.find(property="v:average").get_text()  #豆瓣评分
        except:
            disscore=""
        one_movie_message['movie_name'] = title.strip().replace(",","-")
        one_movie_message['movie_daoyan'] = daoyan.strip()
        one_movie_message["movie_bianju"] = bianju.strip()
        one_movie_message["movie_leixing"] = leixing.strip()[:-1]
        one_movie_message["movie_zhuyan"] = zhuyan.strip()
        one_movie_message["movie_showtime"] = showtime.strip()[:-1]
        one_movie_message["movie_pianchang"] = pianchang.strip()
        one_movie_message["movie_disnum"] = disnum.strip()
        one_movie_message["movie_disscore"] = disscore.strip()
        one_movie_message["movie_summary"] = summary.strip().replace(" ","").replace("\n","")
        return one_movie_message

    #获取短评或者影评的数目
    def parase_dis_num(self,page):
        try:
            word = BeautifulSoup(page).find(class_="count").get_text()
            #(共 7648 条) 获取之后是这样的
            return int(word[2:-2])
        except Exception as e:
            print("获得电影短评条数异常:",e)
            return 0

    #解析电影的短评
    def parase_one_movie_duanping(self,content):
        new_comment_list=[]
        try:
            comment_list = BeautifulSoup(content).find_all(class_="comment")
            for comment in comment_list:
                new_comment_list.append(comment.p.get_text().strip())
                # print(comment.p.get_text().strip()+"\n-------------")
        except Exception as e:
            print("解析电影短评异常：" ,e)
            pass
        return new_comment_list

    #解析电影的影评
    def parase_one_movie_yingping(self,content):
        new_comment_list = []
        try:
            comment_list = BeautifulSoup(content).find_all(class_="middle")
            for comment in comment_list:
                comment_dic = {}
                title = comment.find(class_="title-link").get_text()
                comment_dic["title"]=title.replace(","," ")

                user = comment.find(property="v:reviewer").get_text()
                comment_dic["user"] = user.replace(","," ")

                grade = comment.find(property="v:rating")["title"]
                comment_dic["grade"] = grade

                time = comment.find(property="v:dtreviewed")["content"]
                comment_dic["time"] = time.replace("-","")

                content = comment.find(class_="short-content").get_text().strip().split("\n")[0]
                comment_dic["content"] = content.replace(","," ")
                new_comment_list.append(comment_dic)
        except Exception as e:
            print("解析电影影评异常：", e)
            pass
        return new_comment_list
