## 指定想搜索的豆瓣电影以及想爬取的最大评论数与前TOP的排名
KEYWORD = '地球最后的夜晚'
MAX_COUNT = 220
TOP_NUM = 10

## 指定想要忽略的词
IGNORE = ["电影"]

## 指定python绘制词云的字体路径、图片路径以及保存路径
FONT_PATH = 'resources/SimHei.ttf'
PIC_PATH = 'resources/timg.jpg'
FILE_PATH = 'results/地球最后的夜晚.jpg'

## 指定MongoDB相关配置
MONGO_URL = 'localhost'
MONGO_DB = 'lastnight'
MONGO_TABLE_COMMENTS = 'comments'
MONGO_TABLE_WORDS = 'words'

## 指定生成echarts文件的相关参数
WORD_CLOUD_NAME = 'results/地球最后的夜晚.html'
WORD_CLOUD_TITLE = '地球最后的夜晚'