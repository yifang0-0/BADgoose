class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')
class Test2:

    def __init__(self,foo):
        # 定义初始化函数的时候一定要加双下划线，因为构造函数不应该被其他类访问
        self.foo = foo

    def bar(self):
        print(self.foo)
        print('bar')

def main():
    test = Test('hello')
    # AttributeError: 'Test' object has no attribute '__bar'
    #test.__bar()
    # AttributeError: 'Test' object has no attribute '__foo'
   # print(test.__foo)
    test._Test__bar()
    print(test._Test__foo)
    #通过单个下划线引用类名直接跟两根下划线实现引用

    test2 = Test2('hello2')
    test2.bar()
    print(test2.foo)

if __name__ == "__main__":
    main()