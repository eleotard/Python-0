import sys

try:
	assert len(sys.argv) == 2 #doit etre faux
except:
	print("AssertionError: more than one argument is provided")

try:
	assert int(sys.argv[1])
	print("I'm odd" if int(sys.argv[1]) & 1 else "I'm even")
except:
	print("AssertionError: argument is not an integer")