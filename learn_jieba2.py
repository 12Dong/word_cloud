#使用IF-DIF算法提取出文章关键字最高的权值某几个
from os import path
import jieba.analyse as analyse

d = path.dirname('.')
text_path = 'txt/xiaohuangwen.txt'
text = open(path.join(d,text_path)).read()
for key in analyse.extract_tags(text,10,withWeight=False):
    print(key)
