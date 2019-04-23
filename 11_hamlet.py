#CalHamlet.py

def getText():
    txt = open("hamlet.txt","r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, "")
    return txt

hamletTxt = getText()   
words = hamletTxt.split()   #split方法默认以空格分隔，返回列表

counts = {} #字典
for word in words:  #遍历列表
    counts[word] = counts.get(word,0) + 1#以当前某个英文单词作为键，即{"单词":次数}

items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
