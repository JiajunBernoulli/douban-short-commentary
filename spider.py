import re
import time
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse
from selenium import webdriver
from pyquery import PyQuery as pq
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from config import *
from utils.cut_sentences import get_ord_words, get_words
from utils.draw_pic import draw_wordCloud, draw_bar
# option.set_headless()  ## 该方法已过时，用如下代替
from utils.gene_echarts import gene_wordCloud
from utils.save_mongo import save_to_mongo

# option = webdriver.ChromeOptions()          ##  得到option参数用于设置浏览器属性
# option.add_argument("--headless")           ##  设置浏览器不打开
# brower = webdriver.Chrome(options=option)   ##  初始化Chrome浏览器，传入option参数(可以省略)
brower = webdriver.Chrome()
wait = WebDriverWait(brower, 10)            ##  设置浏览器超时时间

#################### 通过关键词获得id###################
def get_id(keyword):
    try:
        ## 等待输入框加载出来
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#inp-query'))
        )
        ## 输入关键词
        input.send_keys(keyword)
        ## 关键是等待下拉菜单出来，sleep时间可调整
        time.sleep(0.5)
        ## 通过模拟键盘按键选中下拉菜单的第一个电影并跳转
        input.send_keys(Keys.DOWN)
        input.send_keys(Keys.ENTER)
        time.sleep(0.5)
        ## 得到跳转后的url并解析从而获得id
        url = brower.current_url
        result = urlparse(url)
        id = re.findall('\d+', result.path)
        return id[0]
    except TimeoutException:
        ## 请求超时则重新请求
        return get_id(keyword)
#################### 通过关键词获得id###################
#################### 通过id获得评论，其中maxcount为要获取的最大评论数###################
def get_comments(id, maxcount):
    comments = []   ## 用于存储爬取出来的评论
    for count in range(0, maxcount, 20):
        url = "https://movie.douban.com/subject/"+str(id)+"/comments?start="+str(count)+"&limit=20&sort=new_score&status=P"
        print(url)
        try:
            brower.get(url)
            ## 等待最后一条短评加载出来
            wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#comments > div:nth-child(20) > div.comment > p > span'))
            )
            # with open("resources/comments.html", encoding="utf-8") as f: # 利用本地的html解析进行之后的测试，减少请求次数
            #     content = f.read()
            # doc = pq(content)
            ## 获取源码用pyquery解析
            html = brower.page_source
            doc = pq(html)
            items = doc.find('.short').items()
            ## 取出标签中的文字存入评论列表
            for item in items:
                comments.append(item.text())
        except TimeoutException:
            ## 请求超时放弃此页，请求下一页
            print(str(count)+"超时")
            continue
    return comments
#################### 通过id获得评论，其中maxcount为要获取的最大评论数###################
def main():
    ## 请求网页并解析
    brower.get('https://movie.douban.com/')
    id = get_id(KEYWORD)
    comments = get_comments(id, MAX_COUNT)
    brower.close()
    ## 构造记录存入MongoDB
    for comment in comments:
        save_to_mongo(MONGO_TABLE_COMMENTS,{'comment': str(comment)})
    ## 获得排名前10的词语
    ord_list, names, values = get_ord_words(comments, TOP_NUM)
    ## 构造记录存入MongoDB
    for i in range(0, len(ord_list)):
        save_to_mongo(MONGO_TABLE_WORDS, {'NUM': i+1, 'NAME': ord_list[i][0], 'VALUE': ord_list[i][1]})
    ## 利用自己的绘图工具类进行绘图
    draw_wordCloud(get_words(comments))
    draw_bar(names, values)
    ## 利用自己的工具类生成echarts文件
    gene_wordCloud(WORD_CLOUD_NAME, WORD_CLOUD_TITLE, names, values)
if __name__ == '__main__':
    main()