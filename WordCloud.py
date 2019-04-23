import wordcloud
import jieba
from scipy.misc import  imread  #更改词云形状
# mask = imread("fivestart.png")

#读取文件、分词整理，由空格分隔得长文本
#设置并输出词云
#观察结果，优化迭代
f1 = open("新时代中国特色社会主义.txt", "r", encoding="utf-8")
t1 = f1.read()
f1.close()
ls1 = jieba.lcut(t1)
txt1 = " ".join(ls1)

w1 = wordcloud.WordCloud(font_path="msyhl.ttc",\
                            width=1000, height=700, background_color="white",\
                            )
w1.generate(txt1)
w1.to_file(" grwordcloud.png")


