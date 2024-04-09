import sys

try:
    assert len(sys.argv) == 2
except:
    print("AssertionError: more than one argument is provided")

try:
    arg = int(sys.argv[1])
    assert isinstance(arg, int), "argument is not an integer"
    print("I'm odd" if arg & 1 else "I'm even")
except:
    print("AssertionError: argument is not an integer")
