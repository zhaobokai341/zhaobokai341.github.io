#作者：赵博凯
#语言：Python
import random as r
import time as t

# 输入要玩几局
a = input("石头剪刀布玩几局：")
a = int(a)
a1 = 0
b1 = 0
a2 = 0
a3 = 0
b3 = 0
# 打印出游戏规则
print("----------1.石头，2.剪刀，3.布，4.提前终止游戏----------")
# 循环进行游戏
for i in range(a):
    a1 = int(a1)
    b1 = int(b1)
    a2 = int(a2)
    a3 = int(a3)
    b3 = int(b3)
    # 输入玩家选择
    q = input("请输入：")
    # 生成计算机选择
    w = r.choice(("1", "2", "3"))
    # 判断玩家和计算机的选择，并输出结果
    if w == "1":
        if q == "1":
            a2 = a2 + 1
            print("这局平局")
        elif q == "2":
            a1 = a1 + 1
            b3 = b3 + 1
            print("这局计算机赢")
        elif q == "3":
            b1 = b1 + 1
            a3 = a3 + 1
            print("这局你赢")
    if w == "2":
        if q == "2":
            a2 = a2 + 1
            print("这局平局")
        elif q == "3":
            a1 = a1 + 1
            b3 = b3 + 1
            print("这局计算机赢")
        elif q == "1":
            b1 = b1 + 1
            a3 = a3 + 1
            print("这局你赢")
    if w == "3":
        if q == "3":
            a2 = a2 + 1
            print("这局平局")
        elif q == "1":
            a1 = a1 + 1
            b3 = b3 + 1
            print("这局计算机赢")
        elif q == "2":
            b1 = b1 + 1
            a3 = a3 + 1
            print("这局你赢")
    # 如果玩家选择提前终止游戏，则输出结果并退出程序
    if q == "4":
        print("你输了", a1, "回", "计算机输了", b1, "回")
        print("平局了", a2, "回")
        print("你赢了", a3, "回", "计算机赢了", b3, "回")
        if a3 < b3:
            print("你输了")
        elif a3 == b3:
            print("平局")
        else:
            print("你赢了")
        t.sleep(30)
        exit()
# 输出最终结果
print("你输了", a1, "回", "计算机输了", b1, "回")
print("平局了", a2, "回")
print("你赢了", a3, "回", "计算机赢了", b3, "回")
if a3 < b3:
    print("你输了")
elif a3 == b3:
    print("平局")
else:
    print("你赢了")
t.sleep(30)
exit()
