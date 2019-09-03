s = input()

if float(s) <= float(400.00):
    print('Novo salario: ' + '%.2lf' % float(float(s)+((float(s)*int(15))/int(100))))
    print('Reajuste ganho: ' + '%.2lf' % float(((float(s)*int(15))/int(100))))
    print('Em percentual: 15 %')

elif float(s)> float(400.00) and float(s) <= float(800.00):
    print('Novo salario: ' + '%.2lf' % float(float(s)+((float(s)*int(12))/int(100))))
    print('Reajuste ganho: ' + '%.2lf' % float(((float(s)*int(12))/int(100))))
    print('Em percentual: 12 %')

elif float(s)> float(800.00) and float(s) <= float(1200.00):
    print('Novo salario: ' + '%.2lf' % float(float(s)+((float(s)*int(10))/int(100))))
    print('Reajuste ganho: ' + '%.2lf' % float(((float(s)*int(10))/int(100))))
    print('Em percentual: 10 %')

elif float(s)> float(1200.00) and float(s) <= float(2000.00):
    print('Novo salario: ' + '%.2lf' % float(float(s)+((float(s)*int(7))/int(100))))
    print('Reajuste ganho: ' + '%.2lf' % float(((float(s)*int(7))/int(100))))
    print('Em percentual: 7 %')

elif float(s) > float(2000.00):
    print('Novo salario: ' + '%.2lf' % float(float(s) + ((float(s) * int(4)) / int(100))))
    print('Reajuste ganho: ' + '%.2lf' % float(((float(s) * int(4)) / int(100))))
    print('Em percentual: 4 %')
