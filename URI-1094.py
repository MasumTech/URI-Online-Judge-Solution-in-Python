total = int(0)
c = int(0)
r = int(0)
s = int(0)
n = int(input())

for i in range(n):
    r1 = input().split(' ')
    a, b = r1
    total = total + int(a)
    if b=='C':
        c = c+int(a)
    elif b=='R':
        r = r+int(a)
    elif b=='S':
        s = s+int(a)

print('Total: '+ str(total) +' cobaias')
print('Total de coelhos: '+ str(c))
print('Total de ratos: '+ str(r))
print('Total de sapos: '+ str(s))
print('Percentual de coelhos: '+'%.2lf' % ((int(c)*100)/int(total))+' %')
print('Percentual de ratos: '+'%.2lf' % ((int(r)*100)/int(total))+' %')
print('Percentual de sapos: '+'%.2lf' % ((int(s)*100)/int(total))+' %')
