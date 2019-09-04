n = int(input())

for x in range(1,n+1):
    if int(x)%int(2)==int(0):
      print(str(x)+'^'+str(2)+' = '+ str(int(x)*int(x)))