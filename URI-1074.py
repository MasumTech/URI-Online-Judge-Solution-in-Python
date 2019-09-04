n = int(input())
for i in range(n):
    a = int(input())

    if a == int(0):
        print('NULL')

    elif a%int(2)!=int(0):
        if a<int(0):
          print('ODD NEGATIVE')
        else:
          print('ODD POSITIVE')

    elif a%int(2)==int(0):
        if a<int(0):
          print('EVEN NEGATIVE')
        else:
          print('EVEN POSITIVE')

