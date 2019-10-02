a = input()

for i in range(1,(int(a)*4)+1):
    if i%4==0:
        print('PUM')
    else:
        print(i, end=' ')