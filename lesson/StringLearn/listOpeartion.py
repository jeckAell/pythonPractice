nameList = [12,"jdfksal","fsd","1","1",12,12]
setList = "123"


###------------------- 增
#########------append和extend。通过append可以向列表添加元素,通过extend可以将另一个集合中的元素逐一添加到列表中
nameList.append(setList)

for name in nameList:
    print(name)

nameList.extend(setList)


########
print("------------------------增加")
for name in nameList:
    print(name)

'''
结果：
12
jdfksal
fsd
123
-----------------------------
12
jdfksal
fsd
123
1
2
3
'''

#----------------------------修改
#####----直接通过下标来确定要修改的是哪个元素，然后才能进行修改，如 A[1] = "xxx"


#----------------------------查找:in、index、count
# in（存在）,如果存在那么结果为true，否则为false
# not in（不存在），如果不存在那么结果为true，否则false
# index(findThings,startSite,endSite)和count(obj)与字符串中的用法相同.
# index(findThings,startSite,endSite)不存在则会报错,存在则会返回该元素所在位置
# count(obj)返回obj在列表中存在的个数

print("--------------------查找");
if 12 in nameList:
    print("true")
else:
    print("not true")

print(nameList.index("1",0,4))
print(nameList.count(12))

#---------------------------删除：del, pop, remove
print("--------------------pop删除")
nameList.pop()      #pop删除的是最后的一个元素

for temp in nameList:
    print(temp)

print("--------------------remove删除")
nameList.remove("1")             # remove删除指定内容的元素，如果有重复的元素，只删除第一个出现的

for temp in nameList:
    print(temp)


#--------------------------排序：sort,reverse
#sort方法是将list按特定顺序重新排列，默认为由小到大，参数reverse=True可改为倒序，由大到小。
#reverse方法是将list逆置,也就是首位调换
#注意：这个排序方法并没有返回结果，它只是直接在原列表上进行排序操作
#     由于一个列表可以存多种数据类型，所以当整个列表类型不一致或者没有可比性时，sort方法会报错，但是reverse可以用

print("-----------------------------排序")
a = ["ccc","aa","bb"]

a.reverse()
print(a)

a.sort()
print(a)

a.sort(reverse=True)
print(a)

print("-----------------------------不同元素类型的排序")
b = [1,2,"ccc","aa","bb"]

b.reverse()
print(b)

b.sort()
print(b)

b.sort(reverse=True)
print(b)

'''
全部的结果：
12
jdfksal
fsd
1
1
12
12
123
------------------------增加
12
jdfksal
fsd
1
1
12
12
123
1
2
3
--------------------查找
true
3
3
--------------------pop删除
12
jdfksal
fsd
1
1
12
12
123
1
2
--------------------remove删除
12
jdfksal
fsd
1
12
12
123
1
2
-----------------------------排序
['bb', 'aa', 'ccc']
['aa', 'bb', 'ccc']
['ccc', 'bb', 'aa']
-----------------------------不同元素类型的排序
['bb', 'aa', 'ccc', 2, 1]
Traceback (most recent call last):
  File "/home/lt/gitProject/pythonPractice/lesson/StringLearn/listOpeartion.py", line 94, in <module>
    b.sort()
TypeError: unorderable types: int() < str()

Process finished with exit code 1

'''