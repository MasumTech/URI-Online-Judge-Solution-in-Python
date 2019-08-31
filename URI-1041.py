r1 = input().split(" ")
a, b= r1

if float(a)>float(0.0) and float(b)>float(0.0):
    print('Q1')
elif float(a)<float(0.0) and float(b)>float(0.0):
    print('Q2')
elif float(a)<float(0.0) and float(b)<float(0.0):
    print('Q3')
elif float(a)>float(0.0) and float(b)<float(0.0):
    print('Q4')
elif float(a)==float(0.0) and float(b)==float(0.0):
    print('Origem')
elif float(a)==float(0.0) and float(b)!=float(0.0):
    print('Eixo Y')
elif float(a)!=float(0.0) and float(b)==float(0.0):
    print('Eixo X')
