first_row = input().split(" ")
second_row = input().split(" ")

a, b, c = first_row
a1, b1, c1 = second_row

soma = ((int(b)*float(c))+(int(b1)*float(c1)))

print("VALOR A PAGAR: R$ " + '%.2f' % soma)