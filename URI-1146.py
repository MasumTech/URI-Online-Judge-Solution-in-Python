while True:
    a = int(input())
    if a==0:
        break
    else:
         for i in range(1,a):
             print(i,end=' ')
         print(i+1)