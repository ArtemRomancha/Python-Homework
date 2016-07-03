import math
import sys

def ln(a):
	return math.log(a)

def IsPositive(a):
	if a > 0 : 
		return True
	else:
		return False

def ShowPositiveResult(a, b):
	print("ln(%s) = %.6f" % (a, b))

def ShowNegativeResult(a):
	print("ln(%s) is illegal" % a)

def CalculateLn(a):
	arg = float(a)
	if IsPositive(arg):
		ShowPositiveResult(arg, ln(arg))
	else:
		ShowNegativeResult(arg)


def FirstCycle():
	for r in sys.argv[1:]:
		CalculateLn(r)

def SecondCycle():
	for i in range(1, len(sys.argv)):
		CalculateLn(sys.argv[i])

def ThirdCycle():
	i = 1
	while i < len(sys.argv):
		CalculateLn(sys.argv[i])
		i += 1

FirstCycle()
SecondCycle()
ThirdCycle()
#FourthCycle()


