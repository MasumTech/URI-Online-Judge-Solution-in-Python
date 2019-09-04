a = input()
b = input()
sum = int(0)
if int(a)<int(b):
    if int(a)>int(0):
      x = int(int(a)+int(1))
    elif int(a)<int(0):
      x = int(int(a)+int(1))
    y = int(b)
else:
    if int(b)>int(0):
        x = int(int(b)+int(1))
    elif int(b)<int(0):
        x = int(int(b)+int(1))
    y = int(a)

for n in range(int(x),int(y)):
    if int(n)%int(2)!=int(0):
        sum = int(sum) + int(n)

print(sum)