cin = int(0)
cout = int(0)
n = int(input())

for x in range(n):
    a = input()
    if int(a)>=int(10) and int(a)<=int(20):
        cin = int(int(cin)+int(1))
    else:
        cout = int(int(cout)+int(1))

print(str(cin) + ' in')
print(str(cout) + ' out')
