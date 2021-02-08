import sys

a = input("Vedite znach1: ")
b = input("Vedite znach2: ")
c = sys.getsizeof(a)
d = sys.getsizeof(b)
print(c,d)
if min(c,d) == c:
	print("Min: ",a ,"Bayte: ", c)
else:
	print("Min: ",b ,"Bayte: ", d)