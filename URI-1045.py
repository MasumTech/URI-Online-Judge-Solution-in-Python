r1 = input().split(" ")
a, b, c = r1
list = [float(a), float(b), float(c)]
la = sorted(list,reverse=True)
a = la[0]
b = la[1]
c = la[2]

if (float(a)>=(float(b)+float(c))):
    print("NAO FORMA TRIANGULO")

elif ((float(a)*float(a))==((float(b)*float(b))+(float(c)*float(c)))):
    print("TRIANGULO RETANGULO")

elif ((float(a)*float(a))>((float(b)*float(b))+(float(c)*float(c)))):
    print("TRIANGULO OBTUSANGULO")

elif ((float(a)*float(a))<((float(b)*float(b))+(float(c)*float(c)))):
    print("TRIANGULO ACUTANGULO")

if (float(a)==float(b)==float(c)):
    print("TRIANGULO EQUILATERO")

elif (float(a)==float(b)!=float(c)) or (float(a)!=float(b)==float(c)) or (float(a)==float(c)!=float(b)):
    print("TRIANGULO ISOSCELES")
