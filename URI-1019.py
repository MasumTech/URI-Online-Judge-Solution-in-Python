a = int(input())

hr = int(a/3600)
tm = int(a)-int(hr*3600)
min = int(tm/60)
tm = int(tm)-int(min*60)

print(str(hr)+ ':' + str(min)+ ':'+str(tm))
