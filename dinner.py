# -*- coding: utf-8 -*-

"""
Dinner Time Optimizer
dinner.py

Dinner time optimizer using a simple modified genetic annealing algorithm .
"""
from AnswerClasses 	import *

# 				printOutput()
#
# Function to print the input to the program as well as the answer generated
# by the genetic algorithm. Takes in a People object and an array of DayAnswer
# objects. Uses printPeople() and printWeekSolution() functions.
def printOutput(week):
	print "# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
	print "#   ____                                                        #" 
	print "#  (|   \ o                                  o                  #"
	print "#   |    |    _  _    _  _    _   ,_     _|_     _  _  _    _   #" 
	print "#  _|    ||  / |/ |  / |/ |  |/  /  |     |  |  / |/ |/ |  |/   #" 
	print "# (/\___/ |_/  |  |_/  |  |_/|__/   |_/   |_/|_/  |  |  |_/|__  #"
	print "#\t\t\t\t\t\t\t\t#"
	print "# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
	print
	printPeople(week.people)
	print "\nCalculated dinner times:"
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
	for day in range(DINNERS_PER_WEEK):
		print DINNER_DAYS[day] + ": \t" + \
			DINNER_TIMES[week.dayAnswers[day].time] + " -- fit: " + str(week.dayAnswers[day].fitness)
		
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

if __name__  == '__main__':
	weekSolution = WeekAnswer()
	print "here"
	printOutput(weekSolution)