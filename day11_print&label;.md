### print()函数的用法
#### print(a,end=' ') 控制打印后的操作
end表示替换原先每次使用时打印的换行 
#### print("{:n}".format(a)) 控制输出的长度
``` python
print("{:5}".fromat(int(i*j)),end=" ")
```

#### print("-"*50)可以输出规定数量的特殊字符

结果 
（保持了间距一致)
```python
--------------------------------------------------
    1     2     3     4     5     6     7     8     9    10 
    2     4     6     8    10    12    14    16    18    20 
    3     6     9    12    15    18    21    24    27    30 
    4     8    12    16    20    24    28    32    36    40 
    5    10    15    20    25    30    35    40    45    50 
    6    12    18    24    30    36    42    48    54    60 
    7    14    21    28    35    42    49    56    63    70 
    8    16    24    32    40    48    56    64    72    80 
    9    18    27    36    45    54    63    72    81    90 
   10    20    30    40    50    60    70    80    90   100 
--------------------------------------------------

```

### label
a=[1,2,"a","c"]
#### 类型无关
#### 通过索引查找
``` python
>>> a[1]
2
>>> a[-1]
c
#负数索引从右边开始计数，并且从一开始而非从零开始
```
#### 索引与切片操作
```python 
>>> a[1:-1]
[2,'a','c']
>>> a[:]
[1,2,'a','c']
#省略的索引默认填充为最左/最右内容索引值
#当索引左界限过大返回空列表 右界限过大返回左界限后到结束的全部内容
>>> a[1::2]
[2,'c']
#可以设定步长 上行为2（2个里取一个）
*****
>>> a[::-1]
['c','a',2,1]
#表示从默认的第0个开始，步长为1，1步取一个数，但是负数表示倒序，因此由成为一种逆序的方法
```

#### 修改索引内容
可以使用= +直接修改
##### 利用切片清空索引
```python 
>>>a[:]=[]
>>>a
[]
```
#### 判断索引属性
```python 
if a:
    #索引有元素时的操作
else:
    #索引没有元素时的操作
 
len(a)
#可以得到a的元素个数
>>>1 in a
True
>>>8 in a
False
```
#### 常见的索引操作
``` python
a=[1,2,3,4]
a.append(40)
#在列表末尾添加40
a.insert(0,1)
#在位置0处插入1
a.count(2)
#计算列表中2的出现个数
a.remove(1)
#删除列表中的1（指定内容）
del a[-1]
#利用关键字删除右数第一个 （指定位置）
a.reverse()
#倒转整个列表
a.sort()
#默认由小到大
a.extend(b)
#将列表b添加到a的后面

#列表用作栈 后进先出
a.append(34)
a.pop()


#列表用作队列 先进先出
a.pop(0)
>>> for i, j in enumerate(['a', 'b', 'c']):
...     print(i, j)
...
0 a
1 b
2 c
```
#### 列表表达式
列表推导式由包含一个表达式的中括号组成，表达式后面跟随一个 for 子句，之后可以有零或多个 for 或 if 子句。结果是一个列表，由表达式依据其后面的 for 和 if 子句上下文计算而来的结果构成 例如  
a=[x+1 for x in [x** 2 for x in range(3)]]  
x^2+1(0<=x<=3)

### 元组 tuple
元组是由逗号分隔的数据结构 （1，2，3）  
如下操作可行
``` python
x,y,z=(1,2,3)
>>>x
1

x=(123,23)
x=123,
x=(123,)
#当元组只有一个值时 要加一个逗号才会使得赋值成为元组类型  
```
元组不可变，不能增减

### 集合 无序不重复元素集
基本功能包括关系测试和消除重复元素。集合对象还支持 union（联合），intersection（交），difference（差）和 symmetric difference（对称差集）等数学运算。大括号或 set() 函数可以用来创建集合。注意：想要创建空集合，你必须使用 set() 而不是 {}。后者用于创建空字典  
a-b a有b没有 a&b a有b也有 a^b a有b没有或者a没有b有 a|b a有或者b有  
添加操作 a.add('c')
### 字典 无序键值合集
字典是是无序的键值对（key:value）集合，同一个字典内的键必须是互不相同的。一对大括号 {} 创建一个空字典。初始化字典时，在大括号内放置一组逗号分隔的键：值对，这也是字典输出的方式。我们使用键来检索存储在字典中的数据。 
字典的原理就是将原来从0开始的标号改编为自己设定的 给data添加新的元素：  
data={'a':1,'b':'2983'}  
data['c':'23'] #添加新元素
**键只能是不可变值（不能是列表但可以是元组），值可以是可变列表，并且可以动态操作  

#### 字典操作
del data['a'] 删除  
‘a’ in data 查询键是否在字典中 返回true或者false  
data.item() 表示遍历整个字典  
``` python
a = ['Pradeepto', 'Kushal'] 
b = ['OpenSUSE', 'Fedora']
for x, y in zip(a, b): #键在前 值在后
    print("{} uses {}".format(x, y))
#输出
#Pradeepto uses OpenSUSE
#Kushal uses Fedora
```
综合性操作
```python
#!/usr/bin/env python3
n = int(input("Enter the value of n: "))
print("Enter values for the Matrix A")
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])
print("Enter values for the Matrix B")
b = []
for i in range(n):
    b.append([int(x) for x in input().split()])
c = []
for i in range(n):
    c.append([a[i][j] * b[i][j] for j in range(n)])
print("After matrix multiplication")
print("-" * 7 * n)
for x in c:
    for y in x:
        print(str(y).rjust(5), end=' ')
    print()
print("-" * 7 * n)
```

字符串统计单词数：先分割（使用空格‘ ’作为分隔符）成为列表，然后使用len方法统计元素个数  
##### print("the number is {:d}".format(int(len(s.strip().split(" ")))))  


