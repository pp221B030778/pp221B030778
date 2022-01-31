a = int(input())
n = str(input())
if n == "k":
	b = int(input())
	a = a / 1024
	print(round(a,b))
elif n == "b":
	a = a*1024
	print(a)