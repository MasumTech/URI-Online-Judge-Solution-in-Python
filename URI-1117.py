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


