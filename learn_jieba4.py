import sys
import jieba
from os import path
jieba.add_word("大屌")
seg_list = jieba.cut("大屌萌妹人人爱",cut_all=True,HMM=True)
print("myword:"+"/".join(seg_list))