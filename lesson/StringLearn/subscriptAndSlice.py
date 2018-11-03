


# 这个demo是使用字符串的下标和切片

## 下标就是字符串中每一个字符的位置，这个位置是从0开始的

name = "leitaofdefge"

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
# 切片的语法：  字符串名字[起始:结束:步长]，注意结束下标的字符并不会截取进去
# 如果不加步长参数，默认没有步长.所谓步长，就是每隔几个下标截取一次

print(name[0:3])
print(name[0:3:])
print(name[2:4])
print(name[2:])       #截取从2开始到末尾
print(name[:3])       #第一个参数为空，默认为0

print(name[1:-1])     #截取从1开始到末尾倒数第1个
print(name[::3])      #从第0个开始，每隔3个字符截取一个字符
print(name[::-2])     #倒着从最后开始向前截
print(name[1:10:-4])  #返回""
print(name[1:5:2])    #在1到5之间按2步截取
print(name[2:1:3])    #结束位置小于其实位置，返""
print("over");


'''
运行结果
lei
lei
it
itaofdefge
lei
eitaofdefg
ltff
efdote

et

over
'''

#练习，讲一个字符串反转

tempStr = "abcdefg"

print(tempStr[::-1])