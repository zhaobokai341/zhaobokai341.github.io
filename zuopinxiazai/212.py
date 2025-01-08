import tkinter as tk
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from pyperclip import copy
from urllib.parse import quote

Completeness = 0
stop = False
unicode_list = {}
for char in [chr(i) for i in range(0x110000)]:
    try:
        unicode_list[name(char)] = char
    except:
        pass


def not_utf_8():
    get = input_.get()
    utf_8_list = [chr(i) for i in range(32, 127)]
    for i in get:
        if i not in utf_8_list:
            return False
    return True


def close():
    try:
        browser.close()
    except:
        pass
    root.quit()


def search():
    global listbox, stop
    listbox.delete(0, tk.END)
    get = input_.get()
    var.set(f"正在搜索")
    root.update()
    if not_utf_8():
        for i in unicode_list:
            if stop:
                stop = False
                break
            if get.upper() in i:
                listbox.insert(tk.END, f"{i} : {unicode_list[i]}")
                root.update()
    else:
        browser.get(f"https://cn.bing.com/translator?ref=TThis&text={quote(get)}&from=zh-Hans&to=en")
        sleep(2)
        try:
            Elements = browser.find_elements(By.XPATH, '//div[@class="tta_altTransText"]')
            Engilish = [i.text for i in Elements]
            for i in Engilish:
                for j in unicode_list:
                    if stop:
                        break
                    if i.upper() in j:
                        listbox.insert(tk.END, f"{j} : {unicode_list[j]}")
                        root.update()
                if stop:
                    stop = False
                    break
        except Exception as e:
            print(f"错误:{e}")
    if len(listbox.get(0, tk.END)) == 0:
        listbox.insert(tk.END, "找不到哦~~")
        var.set("找不到哦~~")
    else:
        var.set(f"搜索完成，共搜索到{len(listbox.get(0, tk.END))}个结果")


def stop_search():
    global stop
    stop = True


def extract():
    try:
        get = listbox.get(listbox.curselection())
        get = get.split(" : ")
        var2.set(get[0])
        var3.set(get[1])
    except Exception as e:
        var2.set(f"无法提取：{str(e)[0: 15]}...")
        var3.set(f"无法提取：{str(e)[0: 15]}...")


def copy1():
    copy(var2.get())
    var2.set("复制成功")


def copy2():
    copy(var3.get())
    var3.set("复制成功")


root = tk.Tk()
root.title("Unicode搜索")
root.geometry("1500x900")
root.resizable(False, False)
root['background'] = 'royalblue'
var = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()
tk.Label(root, textvariable=var, bg="yellow").pack()
input_ = tk.Entry(root, bg="mediumspringgreen")
input_.pack()
tk.Button(root, text="搜索", command=search, bg="mediumpurple").pack()
tk.Button(root, text="停止搜索", command=stop_search, bg="mediumpurple").pack()
tk.Button(root, text="提取", bg="darkgrey", command=extract).pack()
tk.Label(root, textvariable=var2, bg="salmon", width=50).place(x=50, y=0)
tk.Button(root, text="复制", bg="darkgrey", command=copy1).place(x=430, y=0)
tk.Label(root, textvariable=var3, bg="salmon", width=5).place(x=50, y=50)
tk.Button(root, text="复制", bg="darkgrey", command=copy2).place(x=100, y=50)
var.set(f"正在初始化%{Completeness}")
root.update()
Completeness = 70
var.set(f"正在初始化%{Completeness}")
root.update()
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox = tk.Listbox(root, yscrollcommand=scrollbar.set, height=45, bg="orangered")
listbox.pack(side=tk.TOP, fill=tk.BOTH)
scrollbar.config(command=listbox.yview)
Completeness = 80
var.set(f"正在初始化%{Completeness}")
root.update()
options = Options()
options.add_argument("--headless")
browser = webdriver.Chrome(options=options)
Completeness = 100
var.set(f"正在初始化%{Completeness}")
root.update()
var.set("初始化完成")
root.update()
sleep(1)
var.set("请输入要搜索的Unicode字符关键词")
root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()
