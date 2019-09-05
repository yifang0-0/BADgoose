
#关于@property 和@XXX.setter的用法
----------------------------------------------
'''
然后其实一开始还有些东西不是很懂

有以下这种搞笑的理解
这个相当于把getter和setter封装起来了，那就只能在类方法内调用，对象不能调用？

后来看了一下廖雪峰的网站
貌似有点懂了

property就是把你的这个方法写成一个像属性一样的东西，调用的时候不需要加括号了···

话说我没觉得有多必要···这只不过少写一个括号啊！！！
 可能看起来比较简单吧
比如说你修改age的时候可以同时检查是不是超出了范围

并且如果你没有定义某个属性.setter的话，这个属性（其实是方法）就是只读的
@age.setter
emmmmm这不就是把读和写两个方法写成一个名字吗

我表示不能理解
可能以后用起来会很爽吧···
'''


#关于__slot__的用法
-------------------------------------------------------
'''
假设你创建了一个 animal 类
包含了各种各样的属性

比如 姓名 年龄 毛色 是否直立行走 肤色 牙齿颗数等等500个属性

然后现在有1000个人子类对象和和1000个狗子类对象

显而易见人是不需要毛色属性的
狗也不需要肤色属性

因此使用__slot__=('姓名','年龄'。。。)
就可以防止创建人类对象的时候使用不需要的储存空间

当然 不知道的属性值可以为NULL，但是slot规定之外的属性是不会存在的

而且slot只对当前的类有效，意味者你要生成子类必须要重新规定
'''

#关于子类的用法
------------------------------------------------
'''
就是直接定义然后把object换成父类的名字就好了
'''


#关于抽象类的写法
------------------------------------------------
'''
@abstractmethod
    def make_voice(self):
        """发出声音"""
        pass
'''

#下面是从那个网址里摘过来然后自己修改后的代码
------------------------------------------------------
```python
class Person(object):

    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)
            
    @abstractmethod
    def career(self):
        """输出职业"""
        pass
class Student(Person):
    def __init__(self, name, age):
        self._name = name
        self._age = age
    def career(self):
        print('学生')

def main():
    student = Student('王小锤', 12)
    student.play()
    student._gender = '女'
    student.height = 180
    #student子类可以添加新的属性height
    print(student.height)
    # student.name='~~~'
    # AttributeError: can't set attribute 没有定义修改器是不能对参数进行修改的
    print(student.name)
    #可见进行过property包装的方法可以像属性一样地进行调用
    person = Person('王大锤', 22)
    person.play()
    person._gender = '男'
    #person.height = 180
    # AttributeError: 'Person' object has no attribute 'height'
    print(person)
    
    '''输出
    王小锤正在玩飞行棋.
    180
    王小锤
    王大锤正在玩斗地主.
    <__main__.Person object at 0x000001E48CFF6B88>
    '''

if __name__ == '__main__':
    main()
```
