import sys

def main():
	"""cest le main ici"""

	try:
		assert len(sys.argv) <= 2
	except:
		print("Wrong number of arguments")

	s = None if len(sys.argv) == 1 else sys.argv[1]
	while not s:
		s = input()

	

	# print([i.isupper() for i in s])

	# if len(sys.argv) == 1 or not sys.argv[1]:
	# 	s = input()
	# 	while not s:
	# 		s = input()
	# else:
	# 	s = sys.argv[1]


if __name__ == "__main__":
	main()
