#Continue.py
'''
a
a(1+a)
[a(1+a)](1+a)
...
a(1+a)^N

1.
一年365天，每天进步1%，累积进步 1.01^365
一年365天，每天退步1%，累积退步 0.99^365

2.
一年365天，每天进步1‰，累积进步 1.001^365
一年35天，每天退步1‰，累积退步 0.999^365

3.
一年365天，每天进步5‰或1%，累积进步 1.005^365 1.01^365
一年365天，每天退步5‰或1%，累积退步 0.995^365 0.99^365

4.
一年365天，一周5个工作日，每天进步1%
一年365天，一周2个休息日，每天退步1%

5.
工作日模式要努力到什么水平，才能与每天1%一样？

'''

dayup_1 = pow(1.01, 365)
daydown_1 = pow(0.99, 365)
print(" 向上1%:{:.2f}，\n 向下1%:{:.2f}".format(dayup_1, daydown_1))
print("-------------------------")

dayup_2 = pow(1.001, 365)
daydown_2 = pow(0.999, 365)
print(" 向上1‰:{:.2f}，\n 向下1‰:{:.2f}".format(dayup_2, daydown_2))
print("-------------------------")

dayup_3 = pow(1.005, 365)
daydown_3 = pow(0.995, 365)
print(" 向上5‰:{:.2f}，\n 向下5‰:{:.2f}".format(dayup_3, daydown_3))
print("-------------------------")

dayup_4 = 1.0
dayfactor_4 = 0.01
for i in range(365):
    if i % 7 in [6,0]:
        dayup_4 = dayup_4*(1-dayfactor_4)

    else:
        dayup_4 = dayup_4*(1+dayfactor_4)
print(" 工作日的力量:{:.2f}".format(dayup_4))
print("-------------------------")

def DayUP_5(df):
    dayup_5 = 1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup_5 = dayup_5*(1-0.01)

        else:
            dayup_5 = dayup_5*(1+df)
    return dayup_5

dayfactor_5 = 0.01
while DayUP_5(dayfactor_5) < 37.78:
    dayfactor_5 += 0.001
print(" 工作日的努力参数是:{:.3f}".format(dayfactor_5))




