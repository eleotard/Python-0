import sys
from ft_filter import ft_filter

def main():
	try:
		assert len(sys.argv) == 3
		s = str(sys.argv[1])
		lim = int(sys.argv[2])
		ponctuations = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
		for c in s:
			assert c not in ponctuations
			assert (ord(c) >= 32 and ord(c) <= 126)
	except:
		print("Assertion error: the arguments are bad")
		return 1

	print(ft_filter.__doc__)
	print()
	print(ft_filter(lambda x: len(x) > lim, s.split()))
	# print(ft_filter(None, s.split()))
	# print(list(filter("lalala", s.split())))
	print(list(ft_filter(None, s.split())))

if __name__ == "__main__":
	main()


	# list = [1, 2, 5, 8, 7]
	# print(ft_filter(lambda x: x > 4, list))
	# print()