while True:
       r1 = input().split(' ')
       a, b = r1
       if int(a)==0 or int(b)==0:
          break
       else:
           if(int(a)>0 and int(b)>0):
              print('primeiro')
           elif(int(a)>0 and int(b)<0):
              print('quarto')
           elif (int(a)<0 and int(b)<0):
               print('terceiro')
           elif (int(a)<0 and int(b)>0):
               print('segundo')