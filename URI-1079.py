n = int(input())

for i in range(n):
    r1 = input().split(' ')
    a, b, c = r1
    avg = float(((float(a)*2)+(float(b)*3)+(float(c)*5))/10)
    print('%.1lf' %avg)

