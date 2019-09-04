a = input()
b = input()
c = input()
d = input()
e = input()

n = int(0)
list = [a, b, c, d, e]
sum = float(0.0)

for x in range(len(list)):
    y = float(list[x])
    if float(y)%int(2)==0:
        n = int(int(n) + int(1))

print( str(n) + ' valores pares')
