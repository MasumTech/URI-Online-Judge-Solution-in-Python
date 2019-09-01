r1 = input().split(" ")
a, b, c = r1

if (float(a)<(float(b)+float(c))) and (float(b)<(float(a)+float(c))) and (float(c)<(float(b)+float(a))):
    print('Perimetro = '+ '%.1lf' % float(str(float(a)+float(b)+float(c))))
elif (float(a)>=(float(b)+float(c))) or (float(b)>=(float(a)+float(c))) or (float(c)>=(float(b)+float(a))):
    print('Area = '+ '%.1lf' % float(str(((float(a)+float(b))*float(c))/int(2))))
