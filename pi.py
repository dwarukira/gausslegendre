from decimal import *

getcontext().prec = 3000

a = 1
b = Decimal(1) / Decimal(2).sqrt()
t = Decimal(1) / Decimal(4)
p = 1

for _ in xrange(25):
	an = (a + b) / 2
	b = (a * b).sqrt()
	t -= p * (a - an) ** 2
	p *= 2
	a = an

print ((a + b) ** 2) / (4 * t)