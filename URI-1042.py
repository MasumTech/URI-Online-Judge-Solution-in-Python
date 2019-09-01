r1 = input().split(" ")
a, b, c = r1
list = [int(a), int(b), int(c)]

listA = sorted(list, reverse=False)

a1 = listA[0]
b1 = listA[1]
c1 = listA[2]

print(str(a1)+'\n'+str(b1)+'\n'+str(c1)+'\n\n'+str(a)+'\n'+str(b)+'\n'+str(c))



