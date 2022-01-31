a = str(input())
b = str(input())
if a.count(b) >= 2:
		print(a.find(b),a.rfind(b))
else:
	print(a.find(b))
