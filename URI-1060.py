a = input()
b = input()
c = input()
d = input()
e = input()
f = input()
n = int(0)
list = [a, b, c, d, e, f]

for x in range(len(list)):
    y = float(list[x])
    if float(y)> float(0.0):
        n = int(int(n) + int(1))
print( str(n) + ' valores positivos')