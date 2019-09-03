r1 = input().split(" ")
a, b, c, d = r1

if int(a) > int(c):
  if int(b) > int(d):
    print('O JOGO DUROU '+str((int(24)-int(a))+int(c)-int(1))+' HORA(S) E '+(str((int(60) - int(b)) + int(d)) + ' MINUTO(S)'))
  elif (int(b) < int(d)):
        print('O JOGO DUROU ' + str((int(24) - int(a)) + int(c)) + ' HORA(S) E ' + (str((int(d) - int(b))) + ' MINUTO(S)'))
  elif (int(b) == int(d)):
        print('O JOGO DUROU ' + str((int(24) - int(a)) + int(c)) + ' HORA(S) E ' + str(int(b) - int(d)) + ' MINUTO(S)')


elif (int(a)<int(c)):
    if int(b) > int(d):
        print('O JOGO DUROU ' + str((int(c) - int(a)-int(1))) + ' HORA(S) E '+(str((int(60) - int(b)) + int(d)) + ' MINUTO(S)'))
    elif (int(b) < int(d)):
        print('O JOGO DUROU ' + str((int(c) - int(a))) + ' HORA(S) E ' + (str((int(d) - int(b))) + ' MINUTO(S)'))
    elif (int(b) == int(d)):
        print('O JOGO DUROU ' + str((int(c) - int(a))) + ' HORA(S) E ' + str(int(b) - int(d)) + ' MINUTO(S)')


elif (int(a)==int(c)):
    if int(b) > int(d):
        print('O JOGO DUROU ' + str((int(24) + int(a)) - int(c)-int(1)) + ' HORA(S) E '+(str((int(60) - int(b)) + int(d)) + ' MINUTO(S)'))
    elif (int(b) < int(d)):
        print('O JOGO DUROU ' + str(int(a) - int(c))+ ' HORA(S) E ' + (str((int(d) - int(b))) + ' MINUTO(S)'))
    elif (int(b) == int(d)):
        print('O JOGO DUROU ' + str((int(24) + int(a)) - int(c)) + ' HORA(S) E ' + str(int(b)- int(d)) + ' MINUTO(S)')



