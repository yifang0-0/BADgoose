'''
narcissus 自恋的神仙
好的又复习了一个单词
今年要好好学python呀
一开始以为水仙花数是各位的三次加起来等于总和的
但是其实是表示的意思是自幂数
我原先的认知只是三位的自幂数
所以一开始bug了一晚上···

前一天的想法：
怎么个思路呢
有两种算法吧
一种是1到1000000每一个数字看拆开来是不是每一位的三次之和
那复杂度就是n
第二种方法是从每一位往上推
a**3+b**3+c**3,a++,b++,c++这样
比如1000000以内的水仙花数一定是小于1000000的
所以说运算复杂度应该更低
那我们就计算10位以内水仙花数吧


啊，那么具体怎么从1位到十位呢
我觉得要两个循环
首先bit<=11
由10**bit-1来决定当前数字的上限
首先建立一个十位数组N【10】
初始为全0
起始十位数也是0
bit初始为0
有一个数字位数b
令b==bit
则循环从N【0】到N【b】
期间的N[n]都三次幂后相加得addition
然后就是for i=0 i<bit
i=add(i,bit,n[])
counter++;
if counter==addition(bit,n[])
print(%count)
er
当前位数仍有效时
函数操作int add( a ,limit , n[])
if a<=limit:
    输入当前数字，如果等于9，置为0，将操作权移交下一位 if n[a]==9: n[a]=0 a=add(a+1,limit,n[])
    如果不等于9，加一，结束 else:n[a]++
    return a
然后操作每次都是从最低位开始的，所以在主函数里a=0一开始也搞错了填了i

'''

def add(a ,limit , n):
    if a<=limit:
       if n[a]==9:
           n[a]=0
           a=add(a+1,limit,n)
       else:
           n[a]+=1
    return a

def addition(a,n):
    total=0
    for i in range(a):
        total+=n[i]**a
    return total


bit=0
n=[0,0,0,0,0,0,0,0,0,0]
print(n[1])
counter=0;
for b in range(6):
    i=0
    while i<b:
        re=addition(b,n)
      #  print("%i  %i"%(re,counter))
        if re==counter:
            print("%i:%i"%(b,counter))
            print(n)
        i=add(0,b,n)
        counter+=1



