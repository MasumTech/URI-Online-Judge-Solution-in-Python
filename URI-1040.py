r1 = input().split(" ")
a, b, c, d = r1

avg = ((float(a)*int(2) + float(b)*int(3) + float(c)*int(4) + float(d)*int(1))/float(10.0))

print('Media: ' + '%.1lf' % float(avg))

if avg>= float(7.0):
    print('Aluno aprovado.')
elif avg<float(5.0):
    print('Aluno reprovado.')
elif avg>=float(5.0) and avg<=float(6.9):
    print('Aluno em exame.')
    e = float(input())
    print('Nota do exame: '+ '%.1lf' %float(e))
    if ((avg+e)/int(2)) >= float(5.0):
        print('Aluno aprovado.')
    elif ((avg+e)/int(2))<=float(4.9):
        primnt('Aluno reprovado.')
    print('Media final: '+ '%.1lf' %float(((avg+e)/int(2))))



