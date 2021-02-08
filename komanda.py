import random

a = ["Sezim", "Nazima", "Ali", "Azamat", "Adilet", "Erjan", 
"Aman", "Jalil", "Myktybek", "Kubanychbek", "Nurzat"]

kolvteam = 3

k1 = []
k2 = []
k3 = []
k4 = []
j = 1
while j <= kolvteam:
	h = random.choice(a)
	k1.append(h)
	
	for i in range(int(len(a))):
		if a[i] == h:
			del a[i]
			break
	j+=1
print(k1)

j = 1
while j <= kolvteam:
	h = random.choice(a)
	k2.append(h)
	
	for i in range(int(len(a))):
		if a[i] == h:
			del a[i]
			break
	j+=1
print(k2)

j = 1
while j <= kolvteam:
	h = random.choice(a)
	k3.append(h)
	
	for i in range(int(len(a))):
		if a[i] == h:
			del a[i]
			break
	j+=1
print(k3)

j = 1
while j <= 2:
	h = random.choice(a)
	k4.append(h)
	
	for i in range(int(len(a))):
		if a[i] == h:
			del a[i]
			break
	j+=1
print(k4)

