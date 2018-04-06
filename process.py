# Answer to #3 on Remeeting code quiz
# Run using: python process.py < input.txt > stdout.log 2> stderr.log

import fileinput
import sys
import random

from functools import reduce

RANDOM_LINE_LENGTH = 30 

def read(random_line_length):
	count = 1
	for line in fileinput.input():
		# Print every 10th line on stderr
		if count % 10 == 0:
			sys.stderr.write(line)
		# Print a random line on stdout of length random_line_length
		# Print a random bunch of ascii codes
		random_string = get_random_string(random_line_length)
		sys.stdout.write(random_string)

		count += 1

def get_random_string(string_length):
	# Return string of ascii codes 33-126 randomly
	random_chars = [chr(int(33 + random.random() * (126 - 33))) for _ in range(string_length)]
	return reduce(lambda a, b: str(a) + str(b), random_chars) + '\n'

try:
	read(RANDOM_LINE_LENGTH)
except KeyboardInterrupt:
	sys.exit(0)