import math
r1 = input().split(" ")
r2 = input().split(" ")

a, b = r1
c, d = r2

result = math.sqrt(((float(c)-float(a))**2)+((float(d)-float(b))**2))

print('%.4f' % result)