"""
Dinner Time Optimizer
dinner.py

Dinner time optimizer using a genetic annealing algorithm 
"""
# -*- coding: utf-8 -*-

from numpy import zeros
from DayAnswer import *
from people import *
from random import randint

POSSIBLE_TIMES		= 5 
DINNER_TIMES		= ["6:00", "6:30", "7:00", "7:30", "8:00"]
DINNER_DAYS			= ["Monday", "Tuesday", "Wednesday", "Thursday"]

def createWeekSolution(people):
	weekAnswer = []
	for i in range(DINNERS_PER_WEEK):
		answer = createSolution(people, DINNER_DAYS[i])
		weekAnswer.append(answer)

	return weekAnswer

#				createSolution()
# Creates a DayAnswer solution
#
def createSolution(people, day_id):
	dinnerTime	= randint(0, POSSIBLE_TIMES - 1)
	answer 		= DayAnswer(dinnerTime)
	answer.setFitness(people, day_id)
	return answer

# 				printOutput()
#
# Function to print the input to the program as well as the answer generated
# by the genetic algorithm. Takes in a People object and an array of DayAnswer
# objects. Uses printPeople() and printWeekSolution() functions.
def printOutput(people, week):
	print "~ ~ ~ ~ ~ ~ ~ ~ ~ DINNER TIME ~ ~ ~ ~ ~ ~ ~ ~ ~"
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

		for j in range(0, DINNERS_PER_WEEK):
			# Print day of the week (stylized)
			if j == 0: 	print DINNER_DAYS[j],
			else:		print "\t\t\t\t" + DINNER_DAYS[j],

			# Print times available
			for i in range(0, POSSIBLE_TIMES):
				if str(peep.availability[i + (j * 5)]) == "1":
					print DINNER_TIMES[i],
			print
		print

	print "Number of people: " + str(people.numPeople)

#				printWeekSolution()
#
# Prints the calculated DayAnswer objects for a given 
def printWeekSolution(week):
	for day in range(DINNERS_PER_WEEK):
		print(DINNER_DAYS[day] + ": \t" + DINNER_TIMES[week[day].time] + 
			" -- fit: " + str(week[day].fitness))

if __name__  == '__main__':
	guests = People("data.dinner")
	weekSolution = createWeekSolution(guests)
	printOutput(guests, weekSolution)
