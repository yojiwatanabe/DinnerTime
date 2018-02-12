from people 		import *
from AnswerClasses	import *
from ast			import literal_eval
import struct

'''

# # # # # # # # # # # # PACK SOLUTION INTO 64-BIT WORD # # # # # # # # # # # # #
Order of bits:
	1. Week Fitness 					- - - - - -     32-bit float  
	2. Dinner time 						- - - - - -     24-bit int
		- 8 Dinners, 3 bits each
		- 8 x 3 bits, 24-bit total
	3. Violated heuristic	 			- - - - - -      2-bit int
		- IDs which heuristic was violated, up to four different heuristics
			0. One person can't make it at all
			1. Undetermined
			2. Undetermined
			3. Undetermined
		- Integer will indicate which heuristic was violated
	4. Solution ID			 			- - - - - -		 6-bit int

								  Word
	| ID ||*||	  Dinner time	   ||			Week Fitness 	   |
	[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
	* Violated heuristic
	Each [] = two bits in word
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
'''

FIT_MULTIPLIER 	= 10000

#				packSolution()
#
# Begins packing a WeekAnswer object into a 64-character string. This will make 
# the GA mutations to be much easier and store only key information. Uses 
# pack32() and getSecondWord(). Takes in a WeekAnswer object. Returns a 64-char
# string.
def packSolution(rawSol):
	word 	= int(rawSol.fitness * FIT_MULTIPLIER)
	word 	= pack32(bin(word)[2:]) + pack32(bin(getSecondWord(rawSol))[2:])

	return word

#				pack32()
#
# Fills a string with zeroes until the length is equal to 32. Takes in a string,
# returns a 32-char string.
def pack32(word):
	while len(word) < 32:
		word = "0" + word

	return word

#				getSecondWord()
#
# Calculates the value of all week dinner times pushed into one integer for
# less memory usage. Takes in a WeekAnswer object. Returns a long.
def getSecondWord(rawSol):
	word = long(0)
	for i in range(DINNERS_PER_WEEK):
		mask = rawSol.dayAnswers[i].time << i * 3
		word = mask | word
		# print "time: " + str(rawSol.dayAnswers[i].time)  + "nu word: " + \
		# 	str(word) + " mask: " + str(mask),
		# if (i % 2 == 1): print "\n"
	# print "word: " + str(word)

	return word

#				unpackSolution()
#
# Unpacks a 64-char string into a WeekAnswer struct. Takes in a 64-char string 
# of binary values. Returns a WeekAnswer struct.
def unpackSolution(word):
	# print "~ ~ ~ ~ UNPACKING ~ ~ ~ ~"
	answer 			= WeekAnswer()
	answer.fitness 	= unpackFitness(word)
	# print "Unpacked fitness: " + str(answer.fitness)
	
	unpackTimes(answer, word[33:64])
	answer.updateAttendance()

	return answer

#				unpackFitness()
#
# Unpacks the fitness stored in a 64-char string and returns it as a float. Used
# by unpackSolution and rankSolutions in GeneticAlgs.py.
def unpackFitness(word):
	return float(literal_eval("0b" + word[0:32])) / FIT_MULTIPLIER

#				unpackTimes()
#
# Unpacks dinner times from a 32-char string. Takes in a WeekAnswer object.
# Returns a WeekAnswer object.
def unpackTimes(answer, word):
	wordVal = int(literal_eval("0b" + word))
	for i in range(DINNERS_PER_WEEK): # Retrieve all dinner times stored in word
		temp = (wordVal >> i * 3) & 7
		answer.dayAnswers[i].time = temp
		answer.dayAnswers[i].setFitness(answer.guests, i)
		# print str(i) + " and " + str(temp)

	return answer