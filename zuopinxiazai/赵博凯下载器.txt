#作者：赵博凯
#语言：Python
import tkinter as tk
import requests as req
import tkinter.messagebox as tkbox
from os import system

# 创建主窗口
win = tk.Tk()
win.title('赵博凯下载器')
win['background'] = 'lightblue'
# 在主窗口中添加标签
tk.Label(win, bg='yellow', fg='blue', text="欢迎来到赵博凯下载器").pack()
# 创建垂直和水平滚动条
scroll = tk.Scrollbar(win)
scroll2 = tk.Scrollbar(win)
scroll.pack(side="right", fill="y")
scroll2.pack(side="bottom", fill="x")
# 创建列表框
list = tk.Listbox(win, yscrollcommand=scroll.set, xscrollcommand=scroll2.set, width=50)


# 创建下载函数
def xia():
    # 创建子窗口
    win2 = tk.Tk()
    win2.title('赵博凯下载器')
    win2['background'] = 'lightblue'
    # 在子窗口中添加标签
    tk.Label(win2, bg='yellow', fg='blue', text="请填写下载信息").pack()
    tk.Label(win2, bg='blue', fg='yellow', text="网址：").pack()
    # 创建输入框
    a = tk.Entry(win2, fg="pink")
    a.pack()
    tk.Label(win2, bg='blue', fg='yellow', text="文件名：").pack()
    b = tk.Entry(win2, fg="pink")
    b.insert(0, "D:/新建文件夹/")
    b.pack()
    tk.Label(win2, bg='blue', fg='yellow', text="超时设置：").pack()
    c = tk.Entry(win2, fg="pink")
    c.pack()
    c.insert(0, "None")

    # 创建下载函数
    def xia2():
        global list
        # 获取输入框中的内容
        a2 = a.get()
        b2 = b.get()
        c2 = c.get()
        # 弹出提示框
        tkbox.showinfo(message="正在下载，请稍等")
        try:
            # 设置请求头
            headers = {
                'User-Agent': 'Mozllia/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/53.0.2785.116 Safari/537.36'
            }
            # 发送请求
            d = req.get(url=a2, timeout=eval(c2), headers=headers)
            print(d.status_code)
            # 判断状态码
            if d.status_code != 200:
                tkbox.showerror("访问错误", "状态码：\n" + str(d.status_code))
            else:
                tkbox.showinfo("访问成功", "状态码：\n" + str(d.status_code))
                tkbox.showinfo("开始下载", "开始下载" + str(d.url))
                try:
                    # 保存文件
                    with open(b2, 'wb') as wenjian:
                        wenjian.write(d.content)
                        da = tkbox.askquestion("下载成功", "下载成功，是否打开")
                    if da == "yes":
                        system(b2)
                    # 在列表框中插入下载信息
                    list.insert("end", "网址：" + a2 + ";" + "文件：" + b2)
                except Exception as e:
                    tkbox.showerror("下载错误", "详细信息：\n" + str(type(e)) + "\n" + str(e))
        except Exception as e:
            tkbox.showerror("访问错误", "详细信息：\n" + str(type(e)) + "\n" + str(e))

    # 在子窗口中添加按钮
    tk.Button(win2, bg="yellow", fg="light green", text="一键下载", command=xia2).pack()
    win2.mainloop()


# 在主窗口中添加列表框
list.pack(side="bottom", fill="both")
# 设置滚动条
scroll.config(command=list.yview)
scroll2.config(command=list.xview)
# 在主窗口中添加按钮
tk.Button(win, bg="light green", fg='yellow', text="新建下载任务", command=xia).pack()
win.mainloop()
