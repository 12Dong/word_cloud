#-*- coding = UTF-8 -*-
#添加自定义词库
from __future__ import print_function,unicode_literals
import sys
import jieba
jieba.load_userdict("txt/userdict.txt")
#jieba采用延迟加载 import jieba不会立即出发词典的加载，一旦有必要 才开始加载词典构建trie
#如果你想手工初始jieba 也可以手动
#import jieba
#jieba.initialize() #手动初始化
#在 0.28之前的版本是不能指定主词典的路径的 有了延迟加载机制后 你可以改变主词典的路径
#注意用户 词典为主词典即 优先考虑的词典 原词典此时变为非主词典
#jieba.set_dictionary"data/dict.txt.big"

import jieba.posseg as pseg
'''原 不加新词典
李小福/是/创新/办/主任/也/是/云/计算/方面/的/专家/;/ /什么/是/八/一双/鹿/
/例如/我/输入/一个/带/“/韩玉/赏鉴/”/的/标题/，/在/自定义词/库中/也/增加/了/此/词为/N/类/
/「/台/中/」/正確/應該/不會/被/切開/。/mac/上/可/分出/「/石墨/烯/」/；/此時/又/可以/分出/來凱/特琳/了/。
'''
test_sent = (
"李小福是创新办主任也是云计算方面的专家; 什么是八一双鹿\n"
"例如我输入一个带“韩玉赏鉴”的标题，在自定义词库中也增加了此词为N类\n"
"「台中」正確應該不會被切開。mac上可分出「石墨烯」；此時又可以分出來凱特琳了。"
)
words = jieba.cut(test_sent)
print("/".join(words))
'''
李小福/是/创新办/主任/也/是/云计算/方面/的/专家/;/ /什么/是/八一双鹿/
/例如/我/输入/一个/带/“/韩玉赏鉴/”/的/标题/，/在/自定义词/库中/也/增加/了/此/词为/N/类/
/「/台中/」/正確/應該/不會/被/切開/。/mac/上/可/分出/「/石墨/烯/」/；/此時/又/可以/分出/來/凱特琳/了/。
'''
result = pseg.cut(test_sent)
for i in result :
    print(i)


"""
李小福/nr
是/v
创新办/i
主任/b
也/d
是/v
云计算/x
方面/n
的/uj
专家/n
;/x
 /x
什么/r
是/v
八一双鹿/nz

/x
例如/v
我/r
输入/v
一个/m
带/v
“/x
韩玉赏鉴/nz
”/x
的/uj
标题/n
，/x
在/p
自定义词/n
库中/nrt
也/d
增加/v
了/ul
此/r
词/n
为/p
N/eng
类/q

/x
「/x
台中/s
」/x
正確/ad
應該/v
不/d
會/v
被/p
切開/ad
。/x
mac/eng
上/f
可/v
分出/v
「/x
石墨/n
烯/x
」/x
；/x
此時/c
又/d
可以/c
分出/v
來/zg
凱特琳/nz
了/ul
。/x
"""
