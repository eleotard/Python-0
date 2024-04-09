import sys

def main():
	"""this program print the transposition of a string in morse"""
	try:
		assert len(sys.argv) == 2
		s = str(sys.argv[1])
		for c in s:
			assert c.isalpha() or c.isspace()	
	except:
		print("AssertionError: the arguments are bad")
		return 1

	MORSE_CODE_DICT = { ' ' : '/', 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..' }
	
	s = s.upper()
	for i in s:
		if i in MORSE_CODE_DICT:
			print(f"{MORSE_CODE_DICT[i]}", end='')
	return 0

if __name__ == "__main__":
	main()