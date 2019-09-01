r1 = input().split(" ")
a, b = r1
if (int(a)%int(b)==int(0)) or (int(b)%int(a)==int(0)):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
