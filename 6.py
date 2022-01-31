a = int(input())
k = [0]*a
for i in range (a):
		k[i] = int(input())
for x in range (a):
	if k[x] <= 10:
		print("Go to work!")
	elif k[x] > 10 and k[x] <= 25:
		print("You are weak")
	elif k[x] > 25 and k[x] <= 45:
		print("Okay, fine")
	else:
		print("Burn! Burn! Burn Young!")
