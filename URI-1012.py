row_input = input().split(" ")
a, b, c = row_input

print("TRIANGULO: " + '%.3f' % float((float(a)*float(c))/2))
print("CIRCULO: " + '%.3f' % float(float(3.14159)*float(c)*float(c)))
print("TRAPEZIO: " + '%.3f' % float(((float(a)+float(b))/2)*float(c)))
print("QUADRADO: " + '%.3f' % float(float(b)*float(b)))
print("RETANGULO: " + '%.3f' % float((float(a)*float(b))))