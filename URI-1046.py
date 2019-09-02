r1 = input().split(" ")
a, b = r1

if int(a) > int(b):
    print('O JOGO DUROU '+str((int(24)-int(a))+int(b))+' HORA(S)')
elif (int(a)<int(b)):
    print('O JOGO DUROU ' + str((int(b) - int(a)) )+ ' HORA(S)')
elif (int(a)==int(b)):
    print('O JOGO DUROU '+str((int(24)+int(a))-int(b))+' HORA(S)')
