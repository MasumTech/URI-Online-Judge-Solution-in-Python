a = input()
b = input()

if int(a)>int(b):
  tmp = a
  a = b
  b = tmp
for i in range(int(a)+1, int(b)):
    if i%5==2 or i%5==3:
       print(i)


