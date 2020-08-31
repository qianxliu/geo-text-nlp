# -*- coding: utf-8 -*-
import re
from itertools import groupby
from pyhanlp import *

__all__ = ['get_location', 'extract_locations']

class extractor():
    def __init__(self):
        pass

    def get_location(self, word_pos_list):
        location_list = []
        if word_pos_list==[]:
            return []
        for i,t in enumerate(word_pos_list):
            word = t[0]
            nature = t[1]
            if nature == 'ns':
                loc_tmp = word
                count = i + 1
                while count < len(word_pos_list):
                    next_word_pos = word_pos_list[count]
                    next_pos = next_word_pos[1]
                    next_word = next_word_pos[0]
                    if next_pos=='ns' or 'n' == next_pos[0]:
                        loc_tmp += next_word
                    else:
                        break
                    count += 1
                location_list.append(loc_tmp)

        return location_list # max(location_list)

    def extract_locations(self, text):
        if text=='':
            return []
        seg_list = [(str(t.word), str(t.nature)) for t in HanLP.segment(text)]
        location_list = self.get_location(seg_list)
        return location_list


if __name__ == '__main__':

    text = '新型冠状病毒肺炎（Corona Virus Disease 2019，COVID-19），简称“新冠肺炎”，世界卫生组织命名为“2019冠状病毒病”，是指2019新型冠状病毒感染导致的肺炎。2019年12月以来，湖北省武汉市部分医院陆续发现了多例有华南海鲜市场暴露史的不明原因肺炎病例，现已证实为2019新型冠状病毒感染引起的急性呼吸道传染病。'
    print(extractor().extract_locations(text))
