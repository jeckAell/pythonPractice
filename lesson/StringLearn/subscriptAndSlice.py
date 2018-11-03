


# 这个demo是使用字符串的下标和切片

## 下标就是字符串中每一个字符的位置，这个位置是从0开始的

name = "leitao"

print(name[0])
print(name[1])
print(name[2])
print(name[3])



'''
运行结果
l
e
i
t
'''

# 切片是指对操作的对象截取其中一部分的操作。字符串、列表、元组都支持切片操作。
# 切片的语法：  字符串名字[起始:结束:步长]

print(name[0:3])
print(name[2:4])
print(name[2:])       #截取从2开始到末尾
print(name[1:-1])     #截取从1开始到末尾倒数第1个

'''
运行结果
lei
it
itao
eita
'''