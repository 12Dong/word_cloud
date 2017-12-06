#-*-coding = UTF-8 -*-
#消除中文歧义
import jieba
TestStr = "2010年底部队友谊篮球赛结束"
#因为在汉语中没有空格进行词语的分割，所以经常会出现中文歧义，比如年底-底部-部队-队友
#jieba默认启用了HMM 隐马尔科夫模型 进行中文分词 实际效果不错
seg_list = jieba.cut(TestStr,cut_all=True)
print("Full Mode :"+"/".join(seg_list))
#Full Mode :2010/年底/底部/部队/队友/友谊/篮球/篮球赛/球赛/结束

seg_list = jieba.cut(TestStr,cut_all=False)
print("Default Mode :"+"/".join(seg_list))
#Default Mode :2010/年底/部队/友谊/篮球赛/结束
#在默认模式下有对中文歧义较好的分类方式

seg_list = jieba.cut_for_search(TestStr) #搜索引擎模式
print("Cut for serach :"+"/".join(seg_list))
#Cut for serach :2010/年底/部队/友谊/篮球/球赛/篮球赛/结束