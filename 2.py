a,b = 1,2
sum = 0
while (a<4000000 or b<4000000):
	a, b = b, a+b
	if (b%2==0):
		sum = sum + b
print sum