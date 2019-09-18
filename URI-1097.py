I = float(0)
for i in range(10):
    for j in range(1,4):
        if float(I)!=int(I):
            print('I=' + '%.1lf' % float(I) + ' J=' + '%.1lf' % float(j + I))
        else:
            print('I=' + '%.0lf' % float(I) + ' J=' + '%.0lf' % float(j + I))
    I+=0.2

print('I=2' +  ' J=3')
print('I=2' +  ' J=4')
print('I=2' +  ' J=5')