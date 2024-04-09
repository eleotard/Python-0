from time import sleep
from tqdm import tqdm

# from Loading import ft_tqdm

# for elem in ft_tqdm(range(333)):
# 	sleep(0.005)
# 	print()

i = 0


def display_progress_bar(iterable):
    total_iterations = len(iterable)
    for i, _ in enumerate(iterable):
        progress = ((i + 1) / total_iterations) * 100
        bar_length = 20
        completed_blocks = int(progress / (100 / bar_length))
        remaining_blocks = bar_length - completed_blocks
        bar = '[' + '=' * completed_blocks + ' ' * remaining_blocks + ']'
        print(f'\rProgress: {bar} {progress:.1f}%', end='', flush=True)
        yield _
        time.sleep(0.5)

display_progress_bar(range(20))

def test():
	i = -1
	if i == 2:
		print("lol")
		return
	while 1:
		i += 1
		yield i

for i in test():
	print(i)
# for elem in test():
# 	sleep(0.5)
# 	print(elem)