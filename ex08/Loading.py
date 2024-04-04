import sys
from tqdm import tqdm
import time

# def ft_tqdm(lst: range) -> None:


def main():
	for i in tqdm(range(10)):
		# Simulation d'un traitement long
		time.sleep(0.5)

if __name__ == "__main__":
	main()