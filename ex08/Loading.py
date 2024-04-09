# def ft_tqdm(lst: range) -> None:
#print:
	# nb of iteration
	#temps pris pour faire la boucle [temps pris<temps restant]
		# SI <1s afficher 00:00
	# frequence d iteration par seconde [temps du sleep/it]

import time

# def	count(n):
# 	for i in n:
# 		yield i

lastcall = 0
call_numbers = 0

def ft_tqdm(lst: range) -> None:

	

	return
	# lastcall = 0

	# global lastcall
	# global call_numbers
	# now = time.time_ns()

	# call_numbers += 1
	# print(call_numbers)
	# return [1]
	# # if lastcall:
	# 	time_passed = now - lastcall
	# 	if time_passed * 10**-9 >= 1:
	# 		print(f", {time_passed // 10**9}.{time_passed // 10**7 - (time_passed // 10**9) * 10**2}s/it]", end='')
	# 	else:
	# 		print(f", {round(1 / (time_passed * 10**-9), 2)}it/s]", end='')
	# else:
	# 	print(", ?it/s]", end='')
	# lastcall = now

	# si > 1, (+ d un elem par s)
		# [..., ?it/s] default 
	# si < 1
		# [..., ?s/it]


def main():
	for i in ft_tqdm(range(10)):
		# print(i)
		time.sleep(0.5)
	# ft_tqdm(range(10))
	# time.sleep(0.05)
	# print()
	# ft_tqdm(range(10))
	# time.sleep(0.05)
	# print()
	# ft_tqdm(range(10))
	# time.sleep(0.05)
	# print()


if __name__ == "__main__":
	main()