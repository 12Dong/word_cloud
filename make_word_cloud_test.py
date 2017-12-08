import jieba
import jieba.analyse as analyse
with open("txt/全职高手.txt",'rt') as f:
    text = f.read()
#使用IF-DIF算法提取出文章关键字最高的权值某几个
jieba.add_word("一叶之秋")
for key in analyse.extract_tags(text,20,withWeight=False):
    print(key)
