# douban-short-commentary
爬取豆瓣短评，实现词频的数据可视化。
通过selenium请求，pyquery解析获取短评数据；利用jieba分词提取出词汇频率；使用MongoDB存储爬取的短评以及词语；运用python的pyplot画柱状图，WordCloud画词云，同时生成echarts的词云代码。
config.py中配置相关变量，spider.py实现请求并解析，自己封装的utils下的工具进行可视化处理。
