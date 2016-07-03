import random as r
import sys

if len(sys.argv) > 1:
	n = int(sys.argv[1])

	summ = 0
	for i in range(0, n):
		rand = r.uniform(-1, 1)
		print("%.4f" % rand)
		summ += rand
	
	print("Srednee znachenie = %.4f" % (summ / n))
else: 
	print("SyntaxError, number of random values expecting")
