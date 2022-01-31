a = int(input())
b = [0]*a
stri = "@gmail.com"
for i in range (a):
	b[i] = str(input())
for x in range (a):
	if stri in b[x]:
		print(b[x].replace("@gmail.com"," "))
	