import sys

def test(var):
	var +=1
	return var

def main():
	"""program that takes a string as an argument and print its caracteristics"""

	try:
		assert len(sys.argv) <= 2
	except:
		print("Wrong number of arguments")
		return 1

	upper = lower = space = digit = ponct = 0
	ponctuations = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
	s = None if len(sys.argv) == 1 else sys.argv[1]
	while not s:
		s = input()
	for c in s:
		if c.isupper():
			upper += 1
		elif c.islower():
			lower += 1
		elif c.isdigit():
			digit += 1
		elif c.isspace():
			space += 1
		elif c in ponctuations:
			ponct += 1
	print(f"The text contains {len(s)} characters:")
	print(f"{lower} lower letters")
	print(f"{upper} upper letters")
	print(f"{ponct} ponctuation marks")
	print(f"{space} spaces")
	print(f"{digit} digits")
	return 0
	
if __name__ == "__main__":
	main()

# i.isupper() for i in string
# 1 for c in message if c.isupper()