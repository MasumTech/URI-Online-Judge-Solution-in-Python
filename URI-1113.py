while True:
       r1 = input().split(' ')
       a, b = r1
       if int(a)==int(b):
          break
       else:
           if(int(a)<int(b)):
              print('Crescente')
           elif(int(a)>int(b)):
              print('Decrescente')