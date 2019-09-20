#TempConvert.py
TempStr = input("请输入带有符号的温度值：") # "abcd"-->字符串类类型，''或者""均可以

if TempStr[-1] in ['F','f']:    # []-->列表类型
    C = (eval(TempStr[0:-1])-32 )/1.8
    print("抓换后的温度是{:.2f}C".format(C))
    
elif TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[0:-1])+32
    print("抓换后的温度是{:.2f}F".format(F))
    
else:
    print("输入格式错误")
