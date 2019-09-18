n = int(input())
for i in range(n):
    r1 = input().split(' ')
    a, b = r1
    sum = int(0)

    a = int(a)
    b = int(b)
    if (a>b):
        tmp = b
        b = a
        a = tmp
    a = int(int(a) + int(1))
    for j in range(a, b):
        if(j%2==1):
          sum= sum + j
    print(sum)