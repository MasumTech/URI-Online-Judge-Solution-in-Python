a = float(input())

if float(a)>=float(0.0) and float(a)<=float(25.00):
    print('Intervalo [0,25]')
elif float(a)>=float(25.01) and float(a)<=float(50.00):
    print('Intervalo (25,50]')
elif float(a)>=float(50.01) and float(a)<=float(75.00):
    print('Intervalo (50,75]')
elif float(a)>=float(75.01) and float(a)<=float(100.00):
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')
