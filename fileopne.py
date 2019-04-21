#encoding utf-8

# 写文件
# f = open("test.txt", "w",encoding='utf-8')  #注意这里要加encoding='utf-8'
# f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n")
# f.close()


f = open("test.txt","r",encoding='utf-8') #注意这里要加encoding='utf-8'

# for line in f:
#     print(line, end='')

# result = f.read()
# f.seek(5)
# print(type(len(f.read()))) #sting类型
# print(type(f.read()))		 #int类型


# for i in f.read():
# 	if i=="oas":
# 		print(i)

f.close()