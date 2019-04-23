import turtle

#递归：函数+分支   基例 链条
#字符串反转
def rvs(s):
    if s == "":
        return s
    else:
        return rvs(s[1:])+s[0]  #首字符+其它字符反转

print(rvs("abcdef"))

#斐波那契
def fabna(N):
    if N == 1 or N ==2:
        return 1
    else:
        return fabna(N-1)+fabna(N-2)
print(fabna(8))

#汉诺塔问题
count = 0
def hanoi(n, src, dst, mid):
    global count
    if n == 1:
        print("{}:{}->{}".format(1, src, dst))
        count += 1
    else:
        hanoi(n-1, src, mid, dst)
        print("{}:{}->{}".format(n, src, dst))
        count += 1
        hanoi(n-1, mid, dst, src)
hanoi(3, "A", "C", "B")
print(count)
        
#科赫雪花小包裹
def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size/3, n-1)
        
def main():
    turtle.setup(600, 600)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    level = 3
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.left(-120)   #turtle.right(120)
    koch(400, level)
    turtle.hideturtle()
main()










    
    
