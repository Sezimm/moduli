import os
import random

os.mkdir('/home/sezim/Рабочий стол/Lalalala')
i = 0
while i < 5:
	a = random.randint(1,100000)
	os.mknod(f'/home/sezim/Рабочий стол/Lalalala/t{a}.txt')
	i += 1


