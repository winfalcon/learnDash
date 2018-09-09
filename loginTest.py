#string compare
import sys
name = 'admin'
passwd = '1234'
loginTimes = 0
print('please input user name')
in_a = input()

#  simple 
#if  name == str(in_a):
#    print('enter the passwd')
#    in_p = input()
#    if passwd==str(in_p):
#        print('welcome')
#    else:
#        print('wrong password')
#else:
#    print('Wrong name')    
while name!=str(in_a):
    print('error! please input again')
    in_a = input()
print('name ok, please input password')
in_p = input()
while passwd!=str(in_p):
    print('error! please input password again')
    loginTimes=loginTimes+1
    if int(loginTimes)>4:
        print('error! over retry times')
        sys.exit()
    else:
        in_p = input()

print('welcom'+ str(name)+' to come back')
