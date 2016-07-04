import random
import sys

n = int(sys.argv[1])
counter = 0
for i in range(0, n):
	summ = 0
	for f in range(0, 4):
		r = random.randint(1, 6)
		#print("%i experiment = %i" % (i, r))
		summ += r		
	
	if(summ < 9):
		counter += 1		

probability = counter / n
print("Probability = %.3f" % probability)
