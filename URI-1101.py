while True:
    r1 = input().split(' ')
    a, b = r1
    sum = int(0)
    if int(a)<=0 or int(b)<=0:
        break
    a = int(a)
    b = int(b)
    if (a>b):
        tmp = b
        b = a
        a = tmp
    b = int(int(b) + int(1))
    for j in range(a, b):
        sum= sum + j
        print(j, end=' ')
    print('Sum='+ str(sum))