import os
import time

def running():
    content = '今天又是在秦岭脚下修仙的一天，我好想进城吃kfc啊啊啊啊啊-------'
    while True:
        os.system('cls')
        print(content)
        time.sleep(0.1)
        # sleep的单位是秒
        content = content[1:] + content[0]
        # 将第一个字符放到最后
running()