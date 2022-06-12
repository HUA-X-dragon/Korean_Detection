f=open('ko.txt', encoding='utf8')
line = f.readline().strip() #读取第一行
txt=''
txt += str(line)
while line:  # 直到读取完文件
   line = f.readline().strip()  # 读取一行文件，包括换行符
   txt += str(line)
f.close()  # 关闭文件
