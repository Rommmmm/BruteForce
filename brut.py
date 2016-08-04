#!/usr/bin/python

import itertools
import time
import random
import string


alphabet = (string.letters + string.digits + "-_")

def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

try:
	p_length = int(raw_input("Enter length" + '\n'))
	password = ""
	
	for letter in range(p_length):
    		letter=random.randrange(len(alphabet))
    		password = password + alphabet[letter]
	print("the random pass is %s") % password
except ValueError:
        print ("Error, length must be a number, Exiting...")
	exit()

counter=0
startTime = time.time()

for guess in bruteforce(alphabet,p_length):
	counter+=1
	if guess == password:
		print ("pass is %s") % guess
		print ("It took %d guesses") %counter
		print ('It took {0} seconds.' .format(time.time() - startTime))



