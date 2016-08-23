# -*-coding:utf-8-*-

from urllib import request
from download import down_html
from parase import parase_html
from output import output_all
from url_manager import manage_url
root_url = "https://movie.douban.com/tag/?view=cloud"

class DouBan_Spider(object):
    def __init__(self):
        self.category_dic = {} #用来存储所有热门分类的名字和对应的电影数目,catename和catename_num两个属性
        self.down_class = down_html.DownHtml()  #下载网页
        self.parase_class = parase_html.ParaseHtml() #解析网页
        self.output_class = output_all.OutPut() #存储信息
        self.manage_class = manage_url.UrlManager() #链接管理
        self.tag_right = 1
        self.tag_error = 0

    #获取分类下所有热门分类
    def get_hotcategory(self,url):
        print("get all category!")
        page_content = self.down_class.download(url)
        self.category_dic = self.parase_class.parase_category(page_content)
        self.output_class.output_category(self.category_dic) #将类别信息写入本地文件

    #得到某个类别下所有电影的链接
    def get_one_cate_all_movie_href(self,tag_url):
        page_content = self.down_class.download(tag_url)
        page_num = self.parase_class.parase_pagenum(page_content) #得到该分类总共多少页
        movies_href = []
        try:
            for page in range(int(page_num)):
                page_url = "https://movie.douban.com/tag/%E8%8B%B1%E5%9B%BD?start="+str(page*20)+"&type=T"
                tag_page_content = self.down_class.download(page_url)
                movies_href = self.parase_class.parase_page_all_movies(tag_page_content,movies_href)
                print("all:",page_num,"  right:",self.tag_right,"  error：",self.tag_error,"  page:",page+1,"  URL 获取完毕")
                self.tag_right +=1
        except Exception as e:
            print(e)
            self.tag_error+=1
            pass
        print("该类别下对应的电影数目为：\t",len(movies_href))
        self.output_class.output_all_movies_href(movies_href)
        print("开始获取该类别下对应的电影信息：\n ")
        self.get_one_movie_message(movies_href)      #该类别对应的链接抓取完毕，进行这些链接对应电影信息的抓取

    #下载每个电影的详细信息
    def get_one_movie_message(self,movie_link):
        all_count = 1
        error = 0
        self.manage_class.add_new_urls(movie_link) #将一个类别对应的链接全部加载到manage_url管理的新的链接中
        while(self.manage_class.has_new_url()):
            try:
                one_url = self.manage_class.get_new_url()  #获取一个url
                # one_url=" https://movie.douban.com/subject/1297970/"
                print("Right：",all_count,"  URL:",one_url.strip(),"  ","Error:",error)
                page_content_one = self.down_class.download(one_url)  #下载该网页对应的源代码
                one_movic_dic = self.parase_class.parase_one_movie_message(page_content_one) #解析得到一部电影的具体数据
                id = one_url.split("/")[-2]
                self.output_class.output_one_movie_message(one_movic_dic,id) #将该部电影的数据输出
                all_count+=1
            except Exception as e:
                error +=1
                print(e)
                pass

    #获取每部电影的短评
    def get_one_movie_short_dis(self,movie_url):
        error = 0
        try:
            m_id = movie_url.split("/")[-2]
            movie_url = "https://movie.douban.com/subject/"+str(m_id)+"/comments?sort=new_score"
            short_dis_num = self.parase_class.parase_dis_num(self.down_class.download(movie_url))
            for i in range(int(short_dis_num/20)):  #每页20条数据
                url = "https://movie.douban.com/subject/"+str(m_id)+"/comments?start="+str(i *20)+"&limit=20&sort=new_score"
                duanping_list = self.parase_class.parase_one_movie_duanping(self.down_class.download(url))
                self.output_class.output_duanping(m_id,duanping_list)
                print("ID:",m_id,"Page:",(i+1),"短评写入OK")
        except Exception as e:
            error += 1
            print("电影短评异常:",e)
            pass
        print("ID:", m_id,"短评全部写入OK","异常次数:",error)

    #获取每部电影的影评
    def get_one_movie_long_dis(self,movie_url):
        error = 0
        m_id = movie_url.split("/")[-2]
        movie_url = "https://movie.douban.com/subject/" + str(m_id) + "/reviews"
        long_dis_num = self.parase_class.parase_dis_num(self.down_class.download(movie_url))
        print(long_dis_num)
        for i in range(int(long_dis_num / 20)):  # 每页20条数据
            try:
                url = "https://movie.douban.com/subject/" + str(m_id) + "/reviews?start=" + str(i * 20) + "&filter=&limit=20"
                yingping_list = self.parase_class.parase_one_movie_yingping(self.down_class.download(url))
                self.output_class.output_yingping(m_id, yingping_list)
                print("ID:", m_id, "Page:", (i + 1), "影评写入OK")
            except Exception as e:
                error += 1
                print("电影影评异常:", e)
                pass
        print("ID:", m_id, "影评全部写入OK", "异常次数:", error)

if __name__=="__main__":
    spider = DouBan_Spider()
    '''
    spider.get_hotcategory(root_url)    #获取所有热门分类，，并存储在self.category_dic中
    count = 1
    for cate_name,cate_num in spider.category_dic.items():    #输出所有标签和对应的数目
        tag_url = "https://movie.douban.com/tag/" + request.quote(cate_name)       #将链接中的中文进行转化形成二级tag url
        print(count,"\t标签：",cate_name,"\t数目：",cate_num)
        count += 1  #计数
        spider.get_one_cate_all_movie_href(tag_url)  #得到某个类别下所有电影的链接
    '''
    # while(spider.manage_class.has_new_url()):
    #     spider.get_one_movie_short_dis(spider.manage_class.get_new_url())
    #     spider.get_one_movie_long_dis(spider.manage_class.get_new_url())
    #spider.get_one_movie_short_dis("https://movie.douban.com/subject/5045678/")
    spider.get_one_movie_long_dis("https://movie.douban.com/subject/5045678/")
