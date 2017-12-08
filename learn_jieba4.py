import sys
import jieba
from os import path
#在保留之前代码的基础上 继续添加新的代码出现的效果
#myword:大/屌/萌妹/人人爱
#jieba.add_word("大屌")
#myword:大屌/萌妹/人人爱
#jieba.add_word("萌妹")
#myword:大屌/萌妹/人人爱
#jieba.add_word("屌萌")
#myword:大/屌萌/妹/人人爱
#jieba.add_word("大屌萌妹")
#myword:大屌萌妹/人人爱
seg_list = jieba.cut("大屌萌妹人人爱",cut_all=False,HMM=True)
print("myword:"+"/".join(seg_list))