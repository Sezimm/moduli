import random

a = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", 
"Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
b = []

i = 0
while i < 4:
	b.append(random.choice(a))
	i += 1
print(b)
