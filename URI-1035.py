r1 = input().split()

a, b, c, d = r1

if(int(b)>int(c) and int(d)>int(a) and int(int(c)+int(d))>int(int(a)+int(b)) and int(c)>int(0) and int(d)>int(0) and ((int(a)%int(2)==int(0)))):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
