#Progress.py
import time

scaleOne = 10
print("------执行开始------")
for i in range(scaleOne+1):
    a = '*' * i
    b = '.' * (scaleOne - i)
    c = (i/scaleOne)*100
    print("{:^3.0f}%[{}->{}]".format(c, a, b))
    time.sleep(0.1)
print("------执行结果------")

# 刷新的本质：用后打印的字符信息覆盖之前的字符

scaleTwo = 10
print("\n------执行开始------")
for i in range(scaleTwo+1):
    a = '*' * i
    b = '.' * (scaleTwo - i)
    c = (i/scaleTwo)*100
    print("\r{:^3.0f}%[{}->{}]".format(c, a, b), end="")
    time.sleep(0.1)
print("\n------执行结果------"+"\n")

scaleThree = 20
print("执行开始".center(scaleThree//2, "-"))
start = time.perf_counter()
for i in range(scaleThree+1):
    a = '*' * i
    b = '.' * (scaleThree - i)
    c = (i/scaleThree)*100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end="")
    time.sleep(0.1)
print("\n"+"执行结果".center(scaleThree//2, "-"))









