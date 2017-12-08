# -*- coding=UTF-8 -*-
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
import jieba

#jieba.load_userdict("XXXX")
#添加用户词库为主词典，原词典变为非主词典

from wordcloud import WordCloud,ImageColorGenerator

#获取当前文件路径

d = path.dirname('.')
stopwords = { }
isCN = 1 #默认启用中文分词
back_coloring_path = "img/苏沐橙.jpg"
text_path = 'txt/全职高手.txt'
font_path= 'C:\Windows\Fonts\msyhbd.ttc'
#停用词无
stopwords_path = ''
imgname1 = "WordCloudDefautColor.png"#保存图片的名字1 只按照背景图片形状
imgname2 = "全职词云.png"#保存图片的名字2 颜色按照背景图片颜色布局生成

my_words_list = ["一叶之秋"]  #词库新词
back_coloring = imread(path.join(d,back_coloring_path))#设置背景图片

#设置词云属性
wc = WordCloud(font_path = font_path,#设置字体
               background_color='white',#背景颜色
               max_words = 100, #词云显示最大词数
               mask = back_coloring ,#设置背景图片
               max_font_size = 100, #字体最大值
               random_state = 42 ,
               width = 1000,
               height = 860,
               margin = 2,
               #设置图片默认大小
               )

def add_word(list):
    for items in list:
        jieba.add_word(items)

add_word(my_words_list)

text = open(path.join(d,text_path)).read()

def jiebaclearText(text):
    my_words_list = []
    seg_list = jieba.cut(text,cut_all=False)
    liststr = ' '.join(seg_list)

    #for myword in liststr.split('/'):
      #  if not(myword.strip() in stopwords) and len(myword.strip())>1:
     #       my_words_list.append(myword)
    #return " ".join(my_words_list)
    return liststr
if isCN:
    text = jiebaclearText(text)

wc.generate(text)
image_colors = ImageColorGenerator(back_coloring)

#plt.figure()
#以下代码显示图片

#plt.imshow(wc)
#plt.axis("off")
#plt.show()
#绘制词云
#保存图片 以背景颜色为词云颜色
#wc.to_file(path.join(d,imgname1))
plt.figure()
imge_colors = ImageColorGenerator(back_coloring)
plt.imshow(wc.recolor(color_func=image_colors),interpolation="bilinear")
plt.axis("off")
plt.show()
wc.to_file(path.join(d,imgname2))
