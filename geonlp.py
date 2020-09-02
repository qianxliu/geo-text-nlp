# -*- coding: utf-8 -*-
import re
from itertools import groupby
from pyhanlp import *

import urllib
import urllib.request
import urllib.parse

from bs4 import BeautifulSoup

__all__ = ['get_location', 'extract_locations']

class extractor():
    def __init__(self):
        pass
    
    """
        get location by the pos of the word, such as 'ns'
        eg: get_location('内蒙古赤峰市松山区')
        :param: word_pos_list<list>
        :return: location_list<list> eg: ['陕西省安康市汉滨区', '安康市汉滨区', '汉滨区']
    """
    # 地名词列
    def get_location(self, word_pos_list):
        location_list = []
        if word_pos_list==[]:
            return []
        # i for each time, t for word_pos_list
        for i,t in enumerate(word_pos_list):
            word = t[0]
            nature = t[1]
            # 词性为地名
            if nature == ('ns' or 'gg' or 'nsf' or 'ude2'):
                loc_tmp = word
                count = i + 1
                while count < len(word_pos_list):
                    next_word_pos = word_pos_list[count]

                    # nature
                    next_pos = next_word_pos[1]
                    next_word = next_word_pos[0]
                    if next_pos == ('ns' or 'nsf' or 'gg' or 'ude2') or 'n' == next_pos[0]:
                        loc_tmp += next_word
                    else:
                        break
                    count += 1
                location_list.append(loc_tmp)

        return location_list # max(location_list)

    def extract_locations(self, text):
        if text=='':
            return []
        ## word词 nature词性标注 分词
        seg_list = [(str(t.word), str(t.nature)) for t in HanLP.segment(text)]
        location_list = self.get_location(seg_list)
        return location_list

##def lexical_diversity(text):
    
from collections import Counter


if __name__ == '__main__':

    url = "https://search.sina.com.cn/?range=title&num=20&c=news&col=1_3&sort=time&q="

    key = urllib.parse.quote("新冠肺炎")
    url = url + key

    
    webpage = urllib.request.urlopen(url) # 根据超链访问链接的网页
    data = webpage.read() # 读取超链网页数据
    contents = BeautifulSoup(data, 'html.parser')
##    inputxt = open("input.txt", "rt", encoding='utf-8') # open lorem.txt for reading text
##    contents = inputxt.read()
##    inputxt.close()                   # close the file

    print(contents)
    keywords = extractor().extract_locations(contents.text)

    word_freq = Counter(keywords)
    common_words = word_freq.most_common(10)
    print (common_words)


