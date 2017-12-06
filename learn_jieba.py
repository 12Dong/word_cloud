import jieba

seg_list = jieba.cut("我来到了北京清华大学",cut_all=True,HMM=False)
print("Full Mode: "+"/".join(seg_list)) #全模式
#Full Mode: 我/来到/了/北京/清华/清华大学/华大/大学
#全模式，把句子中所有的可以成词的词语都扫描出来, 速度非常快，但是不能解决歧义；
seg_list = jieba.cut("我来到了北京清华大学",cut_all=False,HMM=True)
print("Default Mode:"+"/".join(seg_list))#默认模式
#Default Mode:我/来到/了/北京/清华大学
#精确模式，试图将句子最精确地切开，适合文本分析；
seg_list = jieba.cut("我们中出现了一个叛徒",cut_all=True,HMM=False)
print("Full Mode : "+"/".join(seg_list))
seg_list = jieba.cut("我们中出了一个叛徒",cut_all=False,HMM=True)
print("Default Mode :"+"/".join(seg_list))
seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造",HMM=False) #搜索引擎模式
print("/".join(seg_list))
#小/明/硕士/毕业/于/中国/科学/学院/科学院/中国科学院/计算/计算所/，/后/在/日本/京都/大学/日本京都大学/深造
#搜索引擎模式，在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。
seg_list = jieba.cut_for_search("大屌萌妹人人爱",HMM=False)
print("/".join(seg_list))
seg_list = jieba.cut("大屌萌妹人人爱",cut_all=False,HMM=True)
print("/".join(seg_list))