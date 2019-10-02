r1 = input().split()
a, b = r1
b = int(b)+int(1)
for i in range(1,int(b)):
     if i%int(a)==0:
         print(i)
     else:
         print(i, end=' ')