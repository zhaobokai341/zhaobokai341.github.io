#作者：赵博凯
#语言：Python
import random as r

print("----------欢迎来到随机生成数----------")
print("1.生成随机整数，2.生成随机小数，3.有随机的规律的整数/小数，4.生成随机元素，5.退出")
fun4 = []
while True:
    fun4 = []
    try:
        # 定义生成随机整数的函数
        def a1():
            fun1 = input("最大范围：")
            fun2 = input("最小范围：")
            fun1 = int(fun1)
            fun2 = int(fun2)
            print("随机整数：", r.randint(fun2, fun1))


        # 定义生成随机小数的函数
        def a2():
            fun1 = input("最大范围：")
            fun2 = input("最小范围：")
            fun3 = input("保留几位小数：")
            fun1 = int(fun1)
            fun2 = int(fun2)
            fun3 = int(fun3)
            print("随机小数：", round(r.uniform(fun2, fun1), fun3))


        # 定义生成有随机规律的整数/小数的函数
        def a3():
            fun1 = input("最大范围：")
            fun2 = input("最小范围：")
            fun3 = input("步长：")
            fun1 = int(fun1)
            fun2 = int(fun2)
            fun3 = int(fun3)
            print("随机数：", r.randrange(fun2, fun1, fun3))


        # 定义生成随机元素的函数
        def a4():
            b = input("要写多少个元素：")
            b = int(b)
            for i in range(b):
                c = input()
                fun4.append(c)
            r.shuffle(fun4)
            print("打乱后的元素：", fun4)


        # 定义退出函数
        def a5():
            print("开始退出，请稍后......")
            exit()


        # 主函数，根据用户输入选择相应的函数
        def main():
            a = input("请选择：")
            if a == "1":
                a1()
            if a == "2":
                a2()
            if a == "3":
                a3()
            if a == "4":
                a4()
            if a == "5":
                a5()


        main()
    except Exception as e:
        print("ERROR", type(e), ":", e)

