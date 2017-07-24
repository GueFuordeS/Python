#! /usr/bin/python3


def power(num, pow, total=1):
	if pow == 0:
		return 1
	if pow > 1:
		total *= num
		return power(num, pow-1, total)
	total *= num
	return total
