import sys
import os
sys.path.append(os.path.abspath(".."))

from ex1.ft_garden_data import Plant

if __name__ == "__main__":
	print("=== Day 1 ===")
	plant1 = Plant("Rose",25,30)
	print("=== Day 7 ===")
	plant1.get_info(7)
