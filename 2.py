a = str(input())
b = 0
for i in a:
	b += ord(i)
if b > 300:
	print("It is tasty!")
else:
	print("Oh, no!")