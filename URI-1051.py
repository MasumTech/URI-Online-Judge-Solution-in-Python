a = input()
x = float(0)
y = float(0)
z = float(0)

if float(a) < float(2000.00):
    print('Isento')
else:
    if float(a)>float(2000) and float(a)<float(3000):
        x = float(float(a) - float(2000.00))
    elif(float(a)>=float(3000)):
        x = float(1000)

    if float(a)>float(3000) and float(a)<float(4500):
        y = float(float(a) - float(3000.00))
    elif(float(a)>=float(4500)):
        y = float(1500)

    if float(a)>float(4500.00):
        z = float(float(a) - float(4500.00))

    sum = float(float(float(x) * float(0.08)) + float(float(y) * float(0.18)) + float(float(z) * float(0.28)))

    print('R$ '+ '%.2lf' % float(sum))


