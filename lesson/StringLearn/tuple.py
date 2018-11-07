
#元祖： 与列表类似。唯一的区别是，元组不能修改。元组使用小括号，列表使用方括号。

#这是基本概念。看起来与队列也没啥区别。但其实最关键的一点是它的语法的灵活和便捷性，提高了编程体验。其中最大的一个特性就是使函数可以返回多个值，这个特性很常用。

#1.函数可以返回多个值

def get_manyValue():
    name = "leitao"
    sex = "man"
    return name,sex

print(get_manyValue())     #可以看到，当有多个返回值的时候，返回的其实是一个元组 ： ('leitao', 'man')

a,b = get_manyValue()   #这里将返回的元组各自赋值给了a和b
print(a)
print(b)

'''
返回结果：
('leitao', 'man')
leitao
man
'''

'''
不仅如此，元组还有如下好处：
相对于 list 而言，tuple 是不可变的，这使得它可以作为 dict 的 key，或者扔进 set 里，而 list 则不行。

tuple 放弃了对元素的增删（内存结构设计上变的更精简），换取的是性能上的提升：创建 tuple 比 list 要快，存储空间比 list 占用更小。所以就出现了“能用 tuple 的地方就不用 list”的说法。

多线程并发的时候，tuple 是不需要加锁的，不用担心安全问题，编写也简单多了。
'''

