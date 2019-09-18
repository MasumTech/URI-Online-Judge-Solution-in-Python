my_dictionary = dict()

for i in range(1,101):
    a = int(input())
    my_dictionary[i] = a
max = int(0)
for j in range(1,101):
    if my_dictionary[j]>=max:
        max = my_dictionary[j]
        p = int(j)

print(max)
print(p)