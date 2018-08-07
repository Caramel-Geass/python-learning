from matplotlib import pyplot as plt


def compound_interest(money, days, rate=0.042):
    dayNum = 1
    while days > 0:
        interest = money * rate / 366
        money = money + interest
        # print('Day ' + str(dayNum) + ':\t' + 'Interest:\t' + str(interest) + '\tTotal:\t' + str(money))
        days = days - 1
        dayNum = dayNum + 1
    return money


'''
# 金融爆炸代码段
year = []
total = []
target = 150
now = 0
money = 10000
while target > 0:
    now = now + 1
    year.append(now)
    money = compound_interest(money, 366)
    total.append(money)
    target = target - 1
plt.plot(year, total)
plt.show()
print(total)

# 攒钱计划代码段
# 计算为1年时间达成储蓄目标，每月需要存钱的多少
target = 14744
total = 0
monthly = 0
while total < target:
    monthly = monthly + 1
    month = 12
    total = 0
    while month > 0:
        totalMonth = total + monthly
        total = compound_interest(totalMonth, 30)
        month = month - 1
    # print('monthly:\t' + str(monthly))

print()
print('Cal done, you should save %s every month' % monthly)
saved = target - 12 * monthly
print('You saved %s Yuan.' % saved)
print()
# 验证
total = 0
month = 12
monthNumber = 1
x = []
y = []
while month > 0:
    totalMonth = total + monthly
    total = compound_interest(totalMonth, 30)
    print(str(monthNumber) + '月：\t' + str(total))
    x.append(monthNumber)
    y.append(total)
    month = month - 1
    monthNumber = monthNumber + 1

plt.plot(x, y)
plt.show()
'''