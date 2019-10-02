a = input()
b = input()
sum = int(0)
if int(a)>int(b):
  tmp = a
  a = b
  b = tmp
for i in range(int(a), int(b)+1):
    if i%13!=0:
        sum +=i

print(sum)
