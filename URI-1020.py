a = int(input())

yr = int(a/365)
days = int(a)-int(yr*365)
mon = int(days/30)
day = int(days)-int(mon*30)

print(str(yr)+ ' ano(s)\n' + str(mon)+ ' mes(es)\n'+str(day)+' dia(s)')
