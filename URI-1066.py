a = input()
b = input()
c = input()
d = input()
e = input()

pr = int(0)
ipr = int(0)
po = int(0)
ne = int(0)
list = [a, b, c, d, e]
sum = float(0.0)

for x in range(len(list)):
    y = int(list[x])
    if int(y)%int(2)==0:
        pr = int(int(pr) + int(1))
    if int(y)%int(2)!=0:
        ipr = int(int(ipr) + int(1))
    if int(y)>int(0):
        po = int(int(po) + int(1))
    if int(y)<int(0):
        ne = int(int(ne) + int(1))


print( str(pr) + ' valor(es) par(es)')
print( str(ipr) + ' valor(es) impar(es)')
print( str(po) + ' valor(es) positivo(s)')
print( str(ne) + ' valor(es) negativo(s)')