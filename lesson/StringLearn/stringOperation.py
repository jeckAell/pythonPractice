

# 此Demo使用一些字符串操作的方法

##########find(childStr,start,end)
# parentStr.find(childStr,start,end),查找某个字符串parentStr中是否包含childStr。存在返回所在位置，否则返回-1
# 注意，当这里输入了查找范围的起始位置时，这个结束的位置包含在查找范围内

parentStr = "leitao is a good student"

print(parentStr.find("good"));
print(parentStr.find("fds"));
print(parentStr.find("good",1,16));
print(parentStr.find("good",1,15));

'''
result：
12
-1
12
-1

'''

############ <模板字符串>.format(<逗号分隔的参数>)
#可以将一个参数按照某种格式化输出
print("{}：计算机{}的CPU 占用率为{}%。".format("2016-12-31","PYTHON",10))
print("{}{}{}".format("圆周率是",3.1415926,"..."))

# format的更多用法课参考：https://blog.csdn.net/i_chaoren/article/details/77922939

'''
2016-12-31：计算机PYTHON的CPU 占用率为10%。
圆周率是3.1415926...
'''

############index(childStr,start,end)
#跟find()方法一样，只不过如果str不在 mystr中会报一个异常.
print(parentStr.index("good",1,16));
# print(parentStr.index("ffdsa"));

'''
result:
12
Traceback (most recent call last):
  File "/home/lt/gitProject/pythonPractice/lesson/StringLearn/stringOperation.py", line 28, in <module>
    print(parentStr.index("ffdsa"));
ValueError: substring not found
'''


##########count(childStr,start,end)
#返回 childStr在start和end之间 在 parentStr里面出现的次数
print(parentStr.count("t"))

'''
3

'''


#由于概念比较简单，有些就不将这些方法一一实现了。

###########replace(str1, str2,  mystr.count(str1))
#把 mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.

###########split(childStr,maxsplit)
#以 childStr 为分割标识进行分割，,maxsplit是分割次数，剩下的没分割的就全部分到一起 返回的是数组
print(parentStr.split(" "))
print(parentStr.split(" ",2))
print(parentStr.split(" ",3))

'''
['leitao', 'is', 'a', 'good', 'student']
['leitao', 'is', 'a good student']
['leitao', 'is', 'a', 'good student']
'''

###########capitalize()
#parentStr.capitalize() 把字符串的第一个字符大写


##########title()
#parentStr.title().把字符串的每个单词首字母大写

##########startswith(childStr)
#检查字符串是否是以 childStr 开头, 是则返回 True，否则返回 False

##########endswith(childStr)
#同上，检查字符串是否以childStr结束，如果是返回True,否则返回 False.

##########lower()
#parentStr.lower() 将所有大写字符为小写

###########upper()
#parentStr.upper() 小写字母为大写

###########ljust(width)
#返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串,width一般要大于本字符串的长度才有效
print(parentStr.ljust(12)+";")
print(parentStr.ljust(30)+";")

'''
leitao is a good student;
leitao is a good student      ;
'''

##########rjust(width)
#返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
print(parentStr.rjust(30));

'''
      leitao is a good student
'''

##########center()
#返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
#原理同上

#########lstrip()
#parentStr.lstrip()   删除 parentStr 左边的空白字符

#########rstrip()
#删除 parentStr 字符串末尾的空白字符

###########strip()
#删除str字符串两端的空白字符


##########rfind()
#类似于 find()函数，不过是从右边开始查找.

##########rindex()
#类似于 index()，不过是从右边开始.

##########partition(str)
#mystr.partition(str) 把mystr以str分割成三部分,str前，str和str后

##########rpartition
#类似于 partition()函数,不过是从右边开始.

##########splitlines()
#按照行分隔，返回一个包含各行作为元素的列表

#########isalpha()
#如果 mystr 所有字符都是字母 则返回 True,否则返回 False

#########isdigit()
#如果 mystr 只包含数字则返回 True 否则返回 False.

########isalnum()
#如果 mystr 所有字符都是字母或数字则返回 True,否则返回 False

########isspace()
#如果 mystr 中只包含空格，则返回 True，否则返回 False.

########join()
#mystr 中每个字符后面插入str,构造出一个新的字符串

