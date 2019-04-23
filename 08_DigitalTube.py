#DigitalTube.py
import turtle
import time

def drawGap():
    turtle.penup()
    turtle.fd(5)
    
def drawLine(draw):     #绘制单段数码管
    drawGap()
    if draw:
        turtle.pendown()
    else:
        turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
    

def drawDigit(digit):   #根据数字绘制七段数码管
    if digit in [2,3,4,5,6,8,9]:    #绘制这些数字需要中间的第一条线
        drawLine(True)
    else:
        drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False) #简写
    if digit in [0,2,3,5,6,8,9]:
        drawLine(True)
    else:
        drawLine(False)
    if digit in [0,2,6,8]:  #绘制第四条线
        drawLine(True)
    else:
        drawLine(False)
    turtle.left(90) #向上继续绘制
    
    if digit in [0,4,5,6,8,9]:  #绘制第五条线
        drawLine(True)
    else:
        drawLine(False)
    if digit in [0,2,3,5,6,7,8,9]:
        drawLine(True)
    else:
        drawLine(False)
    if digit in [0,1,2,3,4,7,8,9]:  #绘制第七条线
        drawLine(True)
    else:
        drawLine(False)
    turtle.left(180)
    turtle.penup()  #为绘制后续数字确定位置
    turtle.fd(40) #为绘制后续数字确定位置
    
def drawDate(date):
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            turtle.write('年',font=("Arial",18,"normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write('月',font=("Arial",18,"normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日',font=("Arial",18,"normal"))
        else:
            drawDigit(eval(i))
            
def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))
    turtle.hideturtle()
    turtle.done()

main()









        
