A = int(0)
G = int(0)
D = int(0)
while True:
     a = int(input())
     if a==1:
         A+=1
         continue
     elif a==2:
         G+=1
         continue
     elif a==3:
         D+=1
         continue
     elif a==4:
         print('MUITO OBRIGADO')
         print('Alcool: '+str(A))
         print('Gasolina: '+str(G))
         print('Diesel: '+str(D))
         break
     else:
         continue
