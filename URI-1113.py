while True:
    r1 = input().split(' ')
    a, b = r1
    if a==b:
        break
    if(a<b):
        print('Crescente')
    elif(b<a):
        print('Decrescente')