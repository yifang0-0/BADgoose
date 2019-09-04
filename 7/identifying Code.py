import random
def identifyingCodeBuilder(a):
    lengthOfCode=a
    source = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lengthOfSource = len(source)
    identifyingCode = ''
    for i in range(lengthOfCode):
        #千万要记得把range填上去，否则老是产生iterable这个错误
        index = random.randint(0,lengthOfSource-1)
        identifyingCode+=source[index]
    return identifyingCode

a=int(input())
print('Your identifying code is %s'%identifyingCodeBuilder(a))