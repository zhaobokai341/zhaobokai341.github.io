from pyperclip import copy


# 定义加密函数
def content1():
    # 判断加密方式
    if types == "1":
        # 加密
        encrypted_and_decrypted1 = encrypted_and_decrypted(contents, True)
    elif types == "2":
        # 解密
        encrypted_and_decrypted1 = encrypted_and_decrypted(contents, False)
    return encrypted_and_decrypted1


# 定义加密和解密函数
def encrypted_and_decrypted(contents1, types1):
    encrypted_or_decrypted = ""
    # 判断加密方式
    if types1:
        # 加密
        for i in contents1: encrypted_or_decrypted += chr(ord(i) + offset)
    else:
        # 解密
        for i in contents1: encrypted_or_decrypted += chr(ord(i) - offset)
    return encrypted_or_decrypted


# 无限循环
while True:
    try:
        # 初始化内容
        contents = ""
        # 输入加密方式
        types = input("请输入加密方式：（1.加密，2.解密，3.退出）：")
        # 判断是否退出
        if types == "3":
            break
        # 判断加密方式是否正确
        if types not in ["1", "2"]:
            print("请输入正确的加密方式！")
            continue
        # 输入内容
        print("请输入内容（多个文件用换行分隔）（exit退出输入）：")
        while True:
            content = input()
            # 判断是否退出输入
            if content == "exit":
                # 去掉最后一个换行符
                contents = list(contents)
                contents[-1] = ""
                contents = ''.join(contents)
                break
            # 添加内容
            contents += content + "\n"
        # 输入偏移量
        offset = int(input("请输入偏移量："))
        # 加密或解密
        encrypted_and_decrypted1 = content1()
        # 输出结果
        print(encrypted_and_decrypted1)
        print(f"---偏移{offset}---")
        # 判断是否复制
        copy1 = input("是否复制？（y/n）：")
        if copy1 == "y":
            # 复制结果
            copy(encrypted_and_decrypted1)
            print("复制成功！")
    # 判断偏移量是否过大
    except ValueError as e:
        if e == 'chr() arg not in range(0x110000)':
            print("偏移量过大！")
        else:
            print("请输入正确的偏移量！")
    # 判断偏移量是否过大
    except OverflowError:
        print("偏移量过大！")
