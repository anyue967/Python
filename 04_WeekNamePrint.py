#WeekNamePrint.py
weekStrOne = "星期一星期二星期三星期四星期五星期六星期日"
weekIdOne = eval(input("请输入星期数字(1-7):"))
posOne = (weekIdOne - 1) * 3
print(weekStrOne[posOne: posOne+3])
print("-------------------------------")

weekStrTwo = "一二三四五六日"
weekIdTwo = eval(input("请输入星期数字(1-7):"))
print("星期" + weekStrTwo[weekIdTwo-1])
print("-------------------------------")

for i in range(12):
    print(chr(9800 +ｉ), end=" ")
print("\n-------------------------------")

