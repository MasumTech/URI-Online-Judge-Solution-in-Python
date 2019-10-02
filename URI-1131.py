I = int(0)
G = int(0)
D = int(0)
C = int(0)
while True:
    r1 = input().split(' ')
    a, b = r1
    print('Novo grenal (1-sim 2-nao)')
    if a>b:
      I = I + 1
    elif a<b:
        G = G + 1
    elif a==b:
        D = D + 1
    x = int(input())
    C = C + 1
    if x == 1:
        continue
    elif x == 2:
        print(str(C) + ' grenais')
        print('Inter:'+ str(I))
        print('Gremio:'+ str(G))
        print('Empates:'+ str(D))
        if a > b:
           print('Inter venceu mais')
        elif a < b:
            print('Gremio venceu mais')
        elif a == b:
            print('Não houve vencedor')
        break



