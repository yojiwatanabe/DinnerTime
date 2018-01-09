from people 		import *
from AnswerClasses	import *
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

MAX_DINNERS	= 8

def binary(num):
    return ''.join(bin(ord(c)).replace('0b', '').rjust(8, '0') \
    	for c in struct.pack('!f', num))

def packSolution(rawSol):
	word = [0, 0]
	word[0] = rawSol.fitness
	word[1] = getSecondWord(rawSol)
	print "Word: ",
	print binary(word[0])

def getSecondWord(rawSol):
	word = long(0)
	for i in range(MAX_DINNERS):
		mask = rawSol.dayAnswers[i] << i
		print mask



