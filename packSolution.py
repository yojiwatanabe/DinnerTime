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

def binary(num):
    return ''.join(bin(ord(c)).replace('0b', '').rjust(8, '0') \
    	for c in struct.pack('!f', num))

def packSolution(rawSol):
	word 		= int(rawSol.fitness * FIT_MULTIPLIER)
	print "TYPE :" + str(type(rawSol.fitness)) + " " + str(word) + " " + bin(word)
	word = pack32(bin(word)[2:]) + pack32(bin(getSecondWord(rawSol))[2:])
	return word

def pack32(word):
	while len(word) < 32:
		word = "0" + word
	return word

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

def unpackSolution(word):
	answer 			= WeekAnswer()
	print "~ ~ ~ ~ UNPACKING ~ ~ ~ ~"
	answer.fitness 	= float(literal_eval("0b" + word[0:32])) / FIT_MULTIPLIER
	print "Unpacked fitness: " + str(answer.fitness)
	unpackTimes(answer, word[33:64])

	return answer

def unpackTimes(answer, word):
	wordVal = int(literal_eval("0b" + word))
	for i in range(DINNERS_PER_WEEK): # Retrieve all dinner times stored in word
		temp = (wordVal >> i * 3) & 7
		# print str(i) + " and " + str(temp)
		answer.dayAnswers[i].time = temp
		
	return answer

def unpackFitness(word):
	return float()
