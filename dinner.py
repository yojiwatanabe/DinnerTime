# -*- coding: utf-8 -*-

"""
Dinner Time Optimizer
dinner.py

Dinner time optimizer using a simple modified genetic annealing algorithm.
"""
from AnswerClasses 	import *
from packSolution 	import *

# 				printIntro()
#
# Overloaded function to print the answer title of the program (in sweet ASCII
# art) and the input data. Takes in a People object. Uses printPeople() function
def printIntro(people = None):
	print "# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
	print "#   ____                                                        #" 
	print "#  (|   \ o                                  o                  #"
	print "#   |    |    _  _    _  _    _   ,_     _|_     _  _  _    _   #" 
	print "#  _|    ||  / |/ |  / |/ |  |/  /  |     |  |  / |/ |/ |  |/   #" 
	print "# (/\___/ |_/  |  |_/  |  |_/|__/   |_/   |_/|_/  |  |  |_/|__  #"
	print "#\t\t\t\t\t\t\t\t#"
	print "# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
	print

	if people != None: printPeople(people)

# 				printOutput()
#
# Function to print the answer generated by the DinnerTime program. Takes in an 
# array of DayAnswer objects. Uses printWeekSolution() function.
def printOutput(week):
	printWeekSolution(week)

#				printPeople()
#
# Prints all of the people in the given People object and their personId. Also
# prints the total number of people in the given object. Used by the 
# printOutput() function but can be called from main for debugging.
# TOADD: Prints when the people are available.
def printPeople(people):
	print "Name\t\tpersonId\tAvailability"

	for peep in people.people:
		print str(peep.name) + "\t\t" + str(peep.personId) + "\t\t",

		for j in range(DINNERS_PER_WEEK):
			# Print day of the week (stylized)
			if j == 0: 	print DINNER_DAYS[j],
			else:		print "\t\t\t\t" + DINNER_DAYS[j],

			# Print times available
			for i in range(POSSIBLE_TIMES):
				if str(peep.availability[i + (j * 5)]) == "1":
					print DINNER_TIMES[i],
			print
		print

	print "Number of people: " + str(people.numPeople)

#				printWeekSolution()
#
# Prints an array of DayAnswer objects that represent a week in dinners. Takes 
# in an array of DayAnswers.
def printWeekSolution(week):
	# Loop print example: "Mon 6:00 - Fit: 100.00 - Att. [1, 1, 1, 1]"
	for day in range(DINNERS_PER_WEEK):
		print("{0:3.3s}".format(DINNER_DAYS[day])), #
		print DINNER_TIMES[week.dayAnswers[day].time] + " - Fit: " \
			+ str.format("{0:6.2f}", week.dayAnswers[day].fitness) + " - Att. "\
			+ str(week.dayAnswers[day].idList), 
		if (day % 2) == 1: print # Print in two columns

	print "Week solution fitness: " + str.format("{0:.2f}", (week.fitness)) \
		+ " - Guest Att. " + str(week.guestAttendance[0:3])

def getSolutions(num):
	weekSolution = [0] * num
	for i in range(num):
		print "WEEK %d" % i
		weekSolution[i] = WeekAnswer()
		printOutput(weekSolution[i])
	return weekSolution
		
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

if __name__  == '__main__':
	printIntro()
	solutions = getSolutions(1)
	word = packSolution(solutions[0])
	print "Word: " + word
	unpackedAnswer	= unpackSolution(word)
	printOutput(unpackedAnswer)
	# print "Unpacked Fit: \t" + str(unpackedAnswer.fitness)
	# print DINNER_TIMES[unpackedAnswer.dayAnswers[0].time] \
	# 	+ " - Att. " + str(unpackedAnswer.dayAnswers[0].idList)
	# print DINNER_TIMES[unpackedAnswer.dayAnswers[1].time] \
		# + " - Att. " + str(unpackedAnswer.dayAnswers[0].idList)
	# print DINNER_TIMES[unpackedAnswer.dayAnswers[2].time] \
	# 	+ " - Att. " + str(unpackedAnswer.dayAnswers[0].idList)
	# print DINNER_TIMES[unpackedAnswer.dayAnswers[3].time] \
	# 	+ " - Att. " + str(unpackedAnswer.dayAnswers[0].idList)
 
