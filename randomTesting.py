#random value testing 
import random

print('I want to play a game!')
print('please in put a number')
inputN = input()
pcN = random.randint(1,10)
#print(random.randint(1, 10))
print('you num is '+str(inputN))
print('pc num is '+str(pcN))
if int(pcN)>int(inputN):
    print('You Lose')
else:
    print('You Win')

 
    