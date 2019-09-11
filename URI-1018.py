a = int(input())
print(int(a))

c = int(a/100)
print(str(c) + ' nota(s) de R$ 100,00')
tk = int(int(a)-int(c)*int(100))

c = int(tk/50)
print(str(c) + ' nota(s) de R$ 50,00')
tk = int(int(tk)-int(c)*int(50))

c = int(tk/20)
print(str(c) + ' nota(s) de R$ 20,00')
tk = int(int(tk)-int(c)*int(20))

c = int(tk/10)
print(str(c) + ' nota(s) de R$ 10,00')
tk = int(int(tk)-int(c)*int(10))

c = int(tk/5)
print(str(c) + ' nota(s) de R$ 5,00')
tk = int(int(tk)-int(c)*int(5))

c = int(tk/2)
print(str(c) + ' nota(s) de R$ 2,00')
tk = int(int(tk)-int(c)*int(2))

print(str(tk) + ' nota(s) de R$ 1,00')