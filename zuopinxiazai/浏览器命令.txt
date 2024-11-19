#作者：赵博凯
#语言：Python
from webbrowser import open as openurl
from time import asctime
from time import sleep
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from chardet import detect
from os import remove

print("正在初始化")
e = "[error]"
w = "[warning]"
ok = "[ok]"
help1 = (
    "baidu(search1) 用百度搜索\nbing(search1) 用Bing搜索\ncalc(Formula) 计算\nclear() 清空屏幕\nclear_content(file) 清空文件内容\n"
    "create(file) 新建文件\n_del(file) 删除文件\ndouyin(search1) 搜索内容 用抖音搜索\n_exit() 退出\ngithub(search1) 搜索内容 用github搜索\n"
    "go_into(url) 去某个网址\n_help() 帮助\n_history() 查看命令\nhot_spot() 热点\nikun_test() 测试你是否是ikun的粉丝\nmoyu() 摸鱼\n"
    "save_help(file) 保存帮助信息\nread(file) 读取文件\nsave_history(file) 保存自己下过的命令信息\nsleep(second) 等待n秒\nnow_time() 显示当前时间\n"
    "translation() 翻译\nwrite_content(file) 写入文件\n数字n（1~无限大）运行自己最近的第n条命令")
edge_options = Options()
edge_options.add_argument('--headless')
edge = webdriver.Edge(options=edge_options)


def search(url, search1):
    global error
    print(ok)
    openurl(url + search1)
    return ok


def ikun(question, A, B, C, answer):
    ikun1 = input(question + f"A.{A} B.{B} C.{C}：")
    if ikun1 == answer or ikun1 == answer.lower():
        print("正确")
        return True
    else:
        print("你不是ikun的粉丝")
        return False


def baidu(search1):
    search("https://www.baidu.com/s?ie=utf-8&wd=", search1)


def bing(search1):
    search("https://cn.bing.com/search?q=", search1)


def calc(Formula):
    global error
    try:
        print(ok, eval(Formula))
        return eval(Formula)
    except:
        print(f"{e}计算失败")
        error = True


def clear():
    print("\033c", end="")
    print(ok)
    return ok


def clear_content(file1):
    global error
    try:
        with open(file1, 'w', encoding="utf-8") as file:
            file.write("")
        print(ok)
        return ok
    except:
        print(f"{e}清除内容失败")
        error = True
        return e


def create(file):
    global error
    try:
        print(ok)
        open(file, 'w').close()
        return ok
    except:
        print(f"{e}保存失败")
        error = True
        return e


def _del(file):
    try:
        remove(file)
        print(ok)
        return ok
    except:
        print(error, "删除失败")
        return error


def douyin(search1):
    search("https://www.douyin.com/search/", search1)


def _exit():
    print(ok, "退出中")
    edge.close()
    exit()


def github(search1):
    search("https://github.com/search?q=", search1)


def go_into(url):
    print(ok)
    openurl(url)
    return ok


def _help():
    print(ok, end="")
    print(help1)
    return help1


def _history():
    if history:
        print(ok)
        for history1 in history:
            print(history1)
        return history
    else:
        print(f"{w}空")
        return ""


def hot_spot():
    try:
        print(ok)
        edge.get("https://top.baidu.com/board?tab=realtime")
        hot_url = edge.find_elements(by=By.XPATH, value='//a[@class="title_dIF3B "]')
        hot_title = edge.find_elements(by=By.XPATH, value='//a[@class="title_dIF3B "]/div[@class="c-single-text-ellipsi'
                                                          's"]')
        hot_title1 = 0
        for hot_url1 in hot_url:
            print(hot_title[hot_title1].text, hot_url1.get_attribute("href"))
            hot_title1 += 1
        return hot_title, hot_url
    except:
        print(f"{e}访问失败")
        return error


def ikun_test():
    True_or_False = ikun("ikun叫什么名字 ", "蔡徐坤", "蔡死坤", "菜就多练", "A")
    if True_or_False:
        True_or_False = ikun("ikun是男的还是女的 ", "女", "无性别", "男", "C")
        if True_or_False:
            True_or_False = ikun("ikun喜欢干什么 ", "唱，跳，rap，打排球", "唱，跳，rap，打篮球", "游泳，rap，打篮球", "B")
            if True_or_False:
                True_or_False = ikun("ikun喜欢唱，跳什么 ", "《鸡你太美》", "《济宁太美》", "《蛇你太美》", "A")
                if True_or_False:
                    print("恭喜你，成为ikun的粉丝")
                    return True


def moyu():
    print(ok, "小提示：Alt+Tab可迅速切换标签页。")
    openurl("https://haiyong.site/moyu/#google_vignette")
    return ok


def save_help(file):
    global error
    try:
        with open(file, 'a') as save_file:
            print(ok)
            save_file.write(help1)
            return ok
    except:
        error = True
        print(f"{e}保存失败")
        return e


def save_history(file):
    global error
    try:
        with open(file, 'a') as save_file:
            print(ok)
            for save_history in history:
                save_file.write(save_history + "\n")
            return ok
    except Exception:
        error = True
        print(f"{e}保存失败")
        return e


def wait(second):
    global error
    print(ok)
    try:
        sleep(second)
        return ok
    except ValueError:
        error = True
        print(f"{e}请输入正确的整数")
        return e


def now_time():
    print(ok, asctime())
    return asctime()


def translation():
    global error
    contents = ""
    print("请输入翻译内容，写/exit终止")
    while True:
        content = input()
        if content == "/exit":
            break
        contents += content + "\n"
    language = input("请输入本地语言（如zh是中文）")
    language1 = input("请输入目标语言（如en是英文）")
    timeout = int(input("请输入翻译延时（秒）"))
    if len(contents) > 1000:
        print(f"{w}应百度翻译要求，最多只能翻译1000给字符，超过不会翻译")
    edge.set_page_load_timeout(timeout)
    try:
        url = f"https://fanyi.baidu.com/mtpe-individual/multimodal?query={contents}&lang={language}2{language1}#/"
        edge.get(url)

    except TimeoutException:
        print("页面超时，停止加载")
    try:
        sleep(1)
        print(ok, edge.find_element(by=By.XPATH, value='//span[@class="_ijgIT8X sentId"]').text)
        return edge.find_element(by=By.XPATH, value='//span[@class="_ijgIT8X sentId"]').text
    except NoSuchElementException:
        print(f"{e}翻译失败")
        error = True
        return e
    except:
        print(f"{e}翻译失败")
        error = True
        return e


def read(file1):
    global error
    try:
        with open(file1, 'rb') as file:
            encoding = detect(file.read())['encoding']
        print(ok)
        with open(file1, encoding=encoding) as file:
            read = file.read()
        print(read)
        return read
    except:
        print(f"{e}读取失败")
        error = True
        return e


def write(file1):
    global error
    print("请输入写入内容：（写/exit终止）")
    contents = ""
    while True:
        content = input()
        if content == "/exit":
            break
        contents += content + "\n"
    try:
        with open(file1, 'a') as file:
            file.write(contents)
        print(ok)
        return ok
    except:
        print(f"{e}写入失败")
        error = True
        return e


print("欢迎，键入_help()可查看帮助，谢谢。")
history = []
while True:
    edge.set_page_load_timeout(1000)
    error = False
    try:
        get = input(">>>")
        if get.isdigit():
            try:
                error = True
                get = history[-int(get)]
                exec(get)
            except IndexError:
                print(f"{e}'{get}'不是变量或命令")
        else:
            try:
                exec(get)
            except NameError:
                print(f"{e}'{get}'不是变量或命令")
                error = True
            except TypeError:
                print(f"{e}参数不正确")
                error = True
            except SyntaxError:
                print(f"{e}语法错误")
            except Exception as q:
                print(type(q), q)
                error = True
        if not error:
            if get != "_history()" and (not get == "") and (not get.isspace()):
                history.append(get)
    except KeyboardInterrupt:
        print(f"{w}已被强制退出")
        edge.close()

