
今天是第四天啦 学习有关GUI的知识
==========================================
tkinter
----------------------------
首先拿到代码https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/10.%E5%9B%BE%E5%BD%A2%E7%94%A8%E6%88%B7%E7%95%8C%E9%9D%A2%E5%92%8C%E6%B8%B8%E6%88%8F%E5%BC%80%E5%8F%91.md
从第一行就开始不认识···

···python
import tkinter
import tkinter.messagebox
···
然后Google了一下，发现Tk包是个自带的做图形用户界面的包，但是我还是pip install Tk了一下，然后貌似发现了一个深入讲解tkinter使用方法的网站<br>
http://thinkingtkinter.sourceforge.net/<br>
有空再来看，现在先存一下


Python Global, Local and Nonlocal variables
------------------------------------------
然后就是函数程序的部分了，首先遇到了 nonlocal ，又不懂，乖乖滚去Google，于是整理一下关于global，local，nonlocal的区别，具体网址在这里https://www.programiz.com/python-programming/global-local-nonlocal-variables<br>
###global
可以从新定义的函数内部接触，相当于全局变量,有下面一些使用规则<br>
0.在外部定义的默认值<br>
1.global可以被内部函数查看，但是不能被修改<br>
2.global关键字仅仅对有效对外无效，比如定义一个A函数内部有一个a函数，如果不特殊定义x在A内local,在a内加关键字global，那么在整个A函数内，a的global定义是无效的，也就是说在嵌套函数内定义global仍然使用的是local属性；只有在调用A函数的时候才会把重新使得内部的global有效（我完全没有搞懂这个操作啊···
  我好像有点理解了，因为在A函数内部，使用的是local的定义，且覆盖了内部嵌套的a的global定义，但是在A函数外部，没有人定义过X了，换句话说没有值能够覆盖这个被定义过的global变量了，因此X的值是由内部的嵌套函数决定的<br>
3.如果想要在内部函数中也能对global进行修改，使用 ‘import config’，并且使用‘config.x’对x进行调用<br>
4.上一条还可以在内部使用global标签，将变量本地化，注意这个全局化是建立在最外层的，所以对于嵌套函数不适用<br>

###local
0.函数内定义的默认值<br>
1.local属性能够覆盖global属性:即同名时在外部定义的global变量会成为内部定义后的local<br>

###nonlocal
0.可以看作global的牛逼版本，因为不能被local覆盖<br>

'''python
import tkinter
import tkinter.messagebox
import config

def main():
    flag = False

    def change_label_text():
        nonlocal flag
        #下面解释一下nonlocal local global的定义
        flag = not flag
        color,msg = ("red","hello,world!")\
            if flag else ('blue','goodbye,world!')
        #这大概是一种神奇的分支语句
        label.config(text = msg,fg = color)

    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('ooooooooooooooops!',"are you sure to quit?"):
            top.quit()

    #顶层窗口
    top = tkinter.Tk()
    #设置窗口大小
    top.geometry('240x240')
    top.title('A Boring Window')
    #创建标签对象并且添加到顶层窗口
    label = tkinter.Label(top,text='Hello,world!',font='rial -32',fg='black')
    label.pack(expand=1)
    #创建按钮容器
    panel1 = tkinter.Frame(top)
    button1 = tkinter.Button(panel1,text='change',command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel1,text='quit',command=confirm_to_quit)
    button2.pack(side='right')
    panel1.pack(side='bottom')
    #开启主事件循环
    tkinter.mainloop()


if __name__ == '__main__':
    main()
'''
[图片]
