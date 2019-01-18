import imageio
from wordcloud import WordCloud
import matplotlib
import matplotlib.pyplot as plt
from config import TOP_NUM, FONT_PATH, PIC_PATH, FILE_PATH
"""
  Created by Jiajun·Bernoulli on 2019/1/18
"""
###########################绘制柱状图#####################
def draw_bar(labels, quants):
    # -*- coding: utf-8 -*-
    print(labels)
    # 指定默认字体
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['font.family'] = 'sans-serif'
    # 解决负号'-'显示为方块的问题
    matplotlib.rcParams['axes.unicode_minus'] = False
    plt.bar(range(len(quants)), quants, color='rgb', tick_label=labels)
    plt.show()

##########################绘制词云########################
def draw_wordCloud(data):
    my_wordcloud = WordCloud(
        background_color='white',  # 设置背景颜色
        max_words=TOP_NUM,  # 设置最大实现的字数
        font_path=FONT_PATH,  # 设置字体格式，如不设置显示不了中文
        mask=imageio.imread(PIC_PATH),  # 设置图片样式
        width=800,
        height=800,
    ).generate_from_frequencies(data)
    plt.figure()
    plt.imshow(my_wordcloud)
    plt.axis('off')
    plt.show()  # 展示词云
    my_wordcloud.to_file(FILE_PATH)