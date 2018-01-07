# -*- coding: utf-8 -*-

"""
Dinner Time Optimizer
dinner.py

Dinner time optimizer using a simple modified genetic annealing algorithm .
"""

from numpy		import zeros
from DayAnswer 	import *
from people 	import *
from random 	import randint

DINNERS_PER_WEEK	= 4
POSSIBLE_TIMES		= 5 
DINNER_TIMES		= ["6:00", "6:30", "7:00", "7:30", "8:00"]
DINNER_DAYS			= ["Monday", "Tuesday", "Wednesday", "Thursday"]

# #				createWeekSolution()
# #
# # Creates an array of DayAnswer solutions to represent an entire week's worth of
# # dinners. Uses createSolution() to generate an answer for each day. Takes in a 
# # People object to pass to createSolution().
# def createWeekSolution(people):
# 	weekAnswer = []
# 	for i in range(DINNERS_PER_WEEK):
# 		answer = createSolution(people, DINNER_DAYS[i])
# 		weekAnswer.append(answer)

# 	return weekAnswer

# #				createSolution()
# #
# # Creates a DayAnswer solution with a pseudorandom dinner time for a given day
# # and already updates the fitness for the answer generated. Takes in a People
# # object and a day_id (e.g. Monday = 0). Used by createWeekSolution().
# def createSolution(people, day_id):
# 	dinnerTime	= randint(0, POSSIBLE_TIMES - 1)
# 	answer 		= DayAnswer(dinnerTime)
# 	answer.setFitness(people, day_id)
# 	return answer

#				variabilityFitness(weekSolution)
#
# Calculates the variability in people of a week solution (struct of DayAnswers)
# and sets the fitness of each week accordingly


# 				printOutput()
#
# Function to print the input to the program as well as the answer generated
# by the genetic algorithm. Takes in a People object and an array of DayAnswer
# objects. Uses printPeople() and printWeekSolution() functions.
def printOutput(people, week):
	print "# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
	print "#   ____                                                        #" 
	print "#  (|   \ o                                  o                  #"
	print "#   |    |    _  _    _  _    _   ,_     _|_     _  _  _    _   #" 
	print "#  _|    ||  / |/ |  / |/ |  |/  /  |     |  |  / |/ |/ |  |/   #" 
	print "# (/\___/ |_/  |  |_/  |  |_/|__/   |_/   |_/|_/  |  |  |_/|__  #"
	print "#\t\t\t\t\t\t\t\t#"
	print "# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
	print
	printPeople(people)
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
		print day
		print DINNER_DAYS[day] + ": \t" + DINNER_TIMES[week.dayAnswers[day].time]
		print	" -- fit: " + str(week.dayAnswers[day])
		
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

if __name__  == '__main__':
	guests = People("data.dinner")
	weekSolution = WeekAnswer
	printOutput(guests, weekSolution)
