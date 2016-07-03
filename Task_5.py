import sys , math

try:	
	outfilename = sys.argv [1]
except:
	print("Usage:", sys.argv[0], "outfile")
	sys.exit (1)

ofile = open(outfilename , "w")

def  myfunc(y):
	if y  >= 0.0:
		return y**5* math.exp(-y)		
	else:
		return  0.0

for i in range(2, len(sys.argv) - 1, 2):
	x = float(sys.argv[i])
	y = float(sys.argv[i + 1])
	fy = myfunc(y)
	ofile.write("%g %g\n" % (x,fy))	
ofile.close()
