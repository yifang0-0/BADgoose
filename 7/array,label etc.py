'''
今天学习python各种数据结构
字符串、列表、元组、集合和字典
'''

# 字符串
# 多种基本操作
def stringLearn():
    a = 'I\'m ironman'
    print(a)
    print(len(a))
    print(a.capitalize())
    # 首字母大写
    print(a.upper())
    # 全部大写
    print(a.find('ironman'))
    print(a.find('Tony'))
    # 寻找字符串出现的首要字节位置，没有找到则输出-1
    print(a.startswith('I'))
    print(a.startswith('you'))
    # 检验是否以设定字符串开头
    print(a.endswith('ironman'))
    # 检验结尾
    print(a.center(15,'~'))
    print(a.ljust(15,'~'))

    string2= '1234567abcde'
    print(string2[-3::-2])
    # ::的操作前一个表示起始位置，如果是负数就从右边开始（注意从右边开始第一位是-1）
    # ::后一个操作数表示的是几个数中取一个，正数表示以选择的数字为基准向右推进，而负数表示向左推进
    # 因为正常顺序是从左向右
    print(string2[-1])
    # 表示输出字符串中的一个字符
    print(string2[-3:-1])
    #表示起始位与结束位 结束位不输出
    print(string2[-1:-3])
    #用：必须起始位小于结束位，只能从左向右输出，否则任何东西都不能被输出
    print(string2[3:-1])
    # 当start_index为正，end_index为负时，同样要遵守物理上起始位小于结束位的规则
    print(string2[-4:10])

#列表
#基本操作
def labelLearn():
    i=[1,2,3,4]
    i[1:2]=['a','b','c','d','e']
    print(i)
    print(len(i))#8
    #切片替换一段，延长列表
    i=[1,2,3,4]
    i[1]=['a','b','c','d','e']
    print(i)
    print(len(i))#4
    #切片替换元素，列表元素个数不变
    # 同时通过切片操作可以替换原有列表中的内容物
    i2=["hello"]
    print(i*5)
    #这个*操作就可以直接复制五遍原先的列表
    list1=[1,1,2,3,5,8,13,21]
    list1.append(200)
    #直接在最后增补
    print(list1)
    print(len(list1))
    list1.insert(1, 400)
    #在1处插入第二个参数，同时其他元素向后移
    print(list1)
    print(len(list1))
    list1 += [1000, 2000]
    #在最后增补
    print(list1)
    print(len(list1))

#集合
def setLearn():
    # 大括号表示集合
    set1 = {1,2,3,4,5,6}
    set2 = {1,3,3,4,7,8}
    print(set1)
    print(set2)
    #集合会自动去掉重复的元素
    set3 = set(range(1,10))
    #注意range（a,b）的元素个数是b-a
    print(set3)
    set4 = set()
    set4.add(11)
    print(set4)
    set4.update([1,2,3])
    print(set4)
    print(set1.pop())
    print(set1)
    print(set1 & set2)
    # print(set1.intersection(set2))
    print(set1 | set2)
    # print(set1.union(set2))
    print(set1 - set2)
    # print(set1.difference(set2))
    print(set1 ^ set2)
    # print(set1.symmetric_difference(set2)) 表示的是xor运算符，即寻找两个集合中不相同的元素
    # 判断子集和超集
    print(set2 <= set1)
    # print(set2.issubset(set1))
    print(set3 <= set1)
    # print(set3.issubset(set1))
    print(set1 >= set2)
    # print(set1.issuperset(set2))
    print(set1 >= set3)
    # print(set1.issuperset(set3))

def dictionaryLearn():
    scorces = {'a':1,'b':3,'c':15}
    print(scorces)
    print(scorces['a'])
    for element in scorces:
        print('%s\t--->\t%d' %(element,scorces[element]))
    scorces['a']=100
    scorces.update(d=1234)
    # 不需要加引号
    print(scorces)
    print(scorces.get('e'))
    print(scorces.get('e',10))
    # 后面设置的是默认值，但是实际上还是没有元素被加入整个字典
    print(scorces.get('e'))
    scorces.popitem()
    # 从后开始弹出元素
    print(scorces)
    scorces.pop('a')
    print(scorces)
    scorces.clear()
    # 保留为一个空的字典
    print(scorces)
'''
{'a': 1, 'b': 3, 'c': 15}
1
a	--->	1
b	--->	3
c	--->	15
{'a': 100, 'b': 3, 'c': 15, 'd': 1234}
None
10
{'a': 100, 'b': 3, 'c': 15}
{'b': 3, 'c': 15}
{}
'''



dictionaryLearn()