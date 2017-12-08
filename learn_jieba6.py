#添加自定义词典/调整词典
import jieba
word = "/".join(jieba.cut("如果放到post中将出错",cut_all=True,HMM=False))
print(word)
word = "/".join(jieba.cut("如果放到post中将出错",cut_all=False,HMM=False))
print(word)
word = "/".join(jieba.cut("如果放到post中将出错把辣椒放到面条中将会变辣",cut_all=False,HMM=False))
print(word)
print(jieba.suggest_freq(("中","将"),True))
word = "/".join(jieba.cut("如果放到post中将出错",cut_all=False,HMM=False))
print(word)
