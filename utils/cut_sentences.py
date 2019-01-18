import jieba as jieba

from config import IGNORE

"""
  Created by Jiajun·Bernoulli on 2019/1/18
"""
########################传入待切割的句子列表，返回无序的words字典(词-次数)###################
def get_words(sentences):
    words = {}
    if not IGNORE is None:
        ignore = IGNORE
    else:
        ignore = [",", "，", ".", "。", " ", "#", "！"]
    for sentence in sentences:
        list = jieba.cut(sentence, cut_all=False)
        for word in list:
            if word in words:
                words[str(word)] = int(words.get(str(word)))+1
            else:
                if not word.isalpha():
                    ignore.append(word)
                    continue
                if word not in ignore:
                    words[str(word)] = 1
    # print(words)
    return words

########################传入待切割的句子列表，返回从高到低排列的有序words列表前count位(词-次数形成的元组)###################
def get_ord_words(sentences, count):
    words = get_words(sentences)
    list = words.items()
    # list.sort(key=cmp_to_key(lambda x, y: cmp(x[1], y[1])))
    ord_list = sorted(list, key=lambda tuple: tuple[1], reverse=True)
    names = []
    values = []
    for i in range(0, len(ord_list)):
        names.append(ord_list[i][0])
        values.append(ord_list[i][1])
    if count is None:
        return ord_list, names, values
    return ord_list[0:count], names[0:count], values[0:count]