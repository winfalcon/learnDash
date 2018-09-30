import random

def getAns():
    return random.randint(1,20)

def printans(value):
    if value == 0:
        print('goal')
    elif value ==1:
        print('too high')
    elif value == 2:        
        print('too low')


def decide(num):
    if int(num) == a :
        return 0
        #print('goal')
    elif int(num) > a :
       # print('too high')
       return 1
    elif int(num) < a:
       # print('too low')       
        return 2

print('please input the number 1-20')
a = getAns()
print(str(a))
aaa = input()
count = 1
while decide(aaa)!=0 :
    printans(decide(aaa))
    aaa = input()
    count = count +1
print('GOAL,You guest '+str(count)+' times')