a = int(input())
i1 = int(0)
i2 = int(0)
for i in range(1,a+1):
    i1 = i*i
    i2 = i*i*i
    print(str(i)+' '+str(i1)+' '+str(i2))
    print(str(i) + ' ' + str(i1+1)+ ' ' + str(i2+1))