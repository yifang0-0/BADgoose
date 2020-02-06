### 实验楼python3简明教程关于collections模块的实验
#### 我写的恶心代码
```python
#!/usr/bin/env python3
import sys
from collections import defaultdict
from collections import Counter
class Person(object):
    """
    \u8fd4\u56de\u5177\u6709\u7ed9\u5b9a\u540d\u79f0\u7684 Person \u5bf9\u8c61
    """

    def __init__(self, name,grade):
        self.name = name
        self.grade = grade

    def get_details(self):
        """
        \u8fd4\u56de\u5305\u542b\u4eba\u540d\u7684\u5b57\u7b26\u4e32
        """
        return self.name


class Student(Person):
    """
    \u8fd4\u56de Student \u5bf9\u8c61\uff0c\u91c7\u7528 name, branch, year 3 \u4e2a\u53c2\u6570
    """

    def __init__(self, name, branch, year):
        Person.__init__(self, name,grade)
        self.branch = branch
        self.year = year

    def count(self):
        con=Counter(grade)
        p=namedtuple("score",['Pass','Fail'])
        c=p(con['A']+con['B']+con['C'],con['D'])
        m=[]
        pa="Pass: "+c.Pass
        m.append(pa)
        fa="Fail: "+c.Fail
        m.append(fa)
        return m
    def get_details(self):
        """
        \u8fd4\u56de\u5305\u542b\u5b66\u751f\u5177\u4f53\u4fe1\u606f\u7684\u5b57\u7b26\u4e32
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)


class Teacher(Person):
    """
    \u8fd4\u56de Teacher \u5bf9\u8c61\uff0c\u91c7\u7528\u5b57\u7b26\u4e32\u5217\u8868\u4f5c\u4e3a\u53c2\u6570
    """
    def __init__(self, name, papers):
        Person.__init__(self, name,grade)
        self.papers = papers
    def count(self):
        c=Counter(grade)
        p=[]
        for i in c:
            m=i+': '+c[i]
            p.append[i]
        return p


    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))


if sys.arg[1]=='teacher':
    teacher1=teacher('a',['a'],sys.argv[2])
    print(','.join(teacher1.count()))
else:
    student1=student('a','a',2005,sys.argv[2])
    print(','.join(student1.count()))

```

#### 参考答案
```python
#!/usr/bin/env python3
import sys
from collections import Counter

class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name

    def get_grade(self):
        return 0


class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, branch, year,grade):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year
        self.grade = grade

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)

    def get_grade(self):

        common = Counter(self.grade).most_common(4)
        n1 = 0
        n2 = 0
        for item in common:
            if item[0] != 'D':
                n1 += item[1]
            else:
                n2 += item[1]
        print("Pass: {}, Fail: {}".format(n1,n2))

class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers, grade):
        Person.__init__(self, name)
        self.papers = papers
        self.grade = grade

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))

    def get_grade(self):
        s = []
        common = Counter(self.grade).most_common(4)
        for i,j in common:
            s.append("{}: {}".format(i,j))
        print(', '.join(s))

person1 = Person('Sachin')
if sys.argv[1] == "student":
    student1 = Student('Kushal', 'CSE', 2005, sys.argv[2])
    student1.get_grade()
else:
    teacher1 = Teacher('Prashad', ['C', 'C++'], sys.argv[2])
    teacher1.get_grade()
```
