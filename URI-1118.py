while True:
     c = float(2.0)
     while True:
            a = input()
            if float(a)>=0 and float(a)<=10:
                break
            else:
                 print('nota invalida')
                 continue
     while True:
           b = input()
           if float(b)>=0 and float(b)<=10:
               break
           else:
               print('nota invalida')
               continue

     print('media = ' + '%.2lf' % float((float(a) + float(b))/float(c)))

     while True:
           x = int(input())
           if x!=1 and x!=2:
               print('novo calculo (1-sim 2-nao)')
               continue
           elif x==2:
               break
           elif x==1:
               break
     if x==1:
         print('novo calculo (1-sim 2-nao)')
         continue
     elif x==2:
         print('novo calculo (1-sim 2-nao)')
         break
