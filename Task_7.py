import random
import sys

n = int(sys.argv[1])
counter = 0
for i in range(0, n):
	for f in range(0, 2):
		r = random.randint(1, 6)
		#print("%i experiment = %i" % (i, r))
		if(r == 6):
			counter += 1
			break
probability = counter / n
print("Probability = %.3f" % probability)
