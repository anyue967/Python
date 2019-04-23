#AutoTraceDraw.py
import turtle as t

t.title("自动绘制轨迹")
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)

#数据读取
# 0-行进距离 1-转向判断 2-转向角度 3-R 4-G 5-B
datals = []
f = open("AutoTraceDraw.txt")
for line in f:
    line = line.replace("\n", "")   #去掉换行字符串
    datals.append(list(map(eval,line.split(","))))
f.close()
#map() 将第一个参数的功能作用与第二个参数的每一个元素

#自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.right(datals[i][2])























    
