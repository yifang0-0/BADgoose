import time
import os
#import subprocess

# 考虑需要实现的方法
# 首先时钟需要能够动态变化，一秒钟重写一次
# 其次需要进位 秒数位是00~59 分钟位是00~59 小时位是00~23

class digitalClock(object):
    def __init__(self,hour=0,minute=0,second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    # 类方法，可以在调用时引发某些动作或者知悉某些函数并且能够自动创建对象
    def now(cls):
        ctime = time.localtime(time.time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
    @staticmethod
    # 类方法，可以在调用时引发某些动作或者知悉某些函数并且能够自动创建对象
    def now2():
        ctime = time.localtime(time.time())
        return  '%02d:%02d:%02d' %(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):

        if self._second == 59:
            self._second = 0

            if self._minute == 59:
                self._minute = 0

                if self._hour == 23:
                    self._hour = 0
                else:
                    self._hour+=1

            else:
                self._minute+=1
        else:
            self._second+=1

    def showClock(self):
           return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():


    clock2 = digitalClock.now2()
    print(type(clock2))
    print("clock2")
    clock = digitalClock.now()
    print(type(clock))
    # print(clock is digitalClocck)
    '''
    这样写是不对的，因为is是判断两个变量的，类感觉不能说是变量
    还学了一个其他的方法
    id()
    用来返回变量的地址，相当于返回指针？
    '''
    print("clock")
    while True:
        i=os.system('cls')
        print(clock.showClock())
        time.sleep(1)
        clock.run()


if __name__ == '__main__':
    main()

'''
然后其实还有些东西不是很懂
比如说这个
@property
这个相当于把getter和setter封装起来了，那就只能在类方法内调用，对象不能调用？
还有
@
'''