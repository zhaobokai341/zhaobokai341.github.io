#作者：赵博凯
#语言：Python
import tkinter as tk
import math as m
import tkinter.messagebox as tkbox

# 创建主窗口
win = tk.Tk()
# 设置窗口背景颜色
win['background'] = "lightblue"
# 设置窗口标题
win.title("计算器")
# 创建一个StringVar对象，用于存储计算结果
var = tk.StringVar()
# 创建一个Label控件，用于显示计算结果
a = tk.Label(win, bg="green", textvariable=var)
# 将Label控件放置在窗口中
a.pack()
# 设置Label控件的初始文本
var.set("输入算式，然后点击Enter键可查看计算结果\n“m”可以调用math模块")
# 创建一个Entry控件，用于输入算式
b = tk.Entry(win, fg="purple")
# 将Entry控件放置在窗口中
b.pack()


# 定义Enter按钮的回调函数
def enter():
    # 获取Entry控件中的文本
    get = b.get()
    # 设置baocun变量为1，用于判断是否保存计算结果
    baocun = 1
    try:
        # 使用eval函数计算算式，并将结果设置为Label控件的文本
        var.set(eval(get))
    except Exception as e:
        # 如果计算出错，将baocun变量设置为0，并弹出错误提示框
        baocun = 0
        tkbox.showerror(title="计算错误", message="详细错误信息：\n" + str(type(e)) + ":" + str(e))
    # 如果计算成功，将计算结果保存到文件中
    if baocun == 1:
        with open("D:\新建文件夹\计算器\历史记录.txt", "a+") as f:
            f.write(get + "=" + str(eval(get)) + "\n")


# 定义查看历史记录按钮的回调函数
def lishi():
    # 弹出提示框，提示用户查看历史记录文件
    tkbox.showinfo(message="请到D:\新建文件夹\计算器\历史记录.txt中查看")


# 创建一个Button控件，用于触发计算
c = tk.Button(win, bg="red", text="Enter", command=enter)
# 将Button控件放置在窗口中
c.pack()
# 创建一个Button控件，用于查看历史记录
d = tk.Button(win, bg="yellow", text="查看历史记录", command=lishi)
# 将Button控件放置在窗口中
d.pack()
# 进入主循环
win.mainloop()
