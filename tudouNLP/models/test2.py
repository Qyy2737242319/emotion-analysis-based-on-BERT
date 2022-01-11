import os

print(os.getcwd())

f = open("./tudouNLP/models/bert_config.json","r")#二进制格式读文件
i = 0
while i<100:
    i += 1 
    print(i)
    line = f.readline()
    if not line:
        break
    else:
        try:
#             print(line)
#             print(line.decode('utf8'))
            line.decode('utf8')
            #为了暴露出错误，最好此处不print
        except:
            print(str(line))

