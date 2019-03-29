import chardet  # 导包

f = open('实验.txt', 'rb')  # 打开文件
for i in f:  # 取出内容，根据文件大小，可取一行进行判断
    a = chardet.detect(i)
    print(a)
f.close()


