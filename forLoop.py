# testing for loop option

print('please input the range')
rangeN = input()
rangeN = int(rangeN)+1
for i  in range(2,int(rangeN)):
    for j in range(1,10):
        print(str(i)+'*'+str(j)+'='+ str(int(i*j)))
    print('\n')