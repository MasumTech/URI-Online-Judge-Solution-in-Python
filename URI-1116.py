n = int(input())

for i in range(n):
    r1 = input().split(' ')
    a, b = r1
    if int(b)==0:
        print('divisao impossivel')
    else:
        print('%.1lf' % (int(a)/int(b)))