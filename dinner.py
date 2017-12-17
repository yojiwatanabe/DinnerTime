"""
Dinner Time Optimizer
dinner.py

Dinner time optimizer using a genetic annealing algorithm 
"""
from people import *
# class Dinner(People):
# 	def __init__(self, filename):
# 		filestream 	= file.open(filename, "r")
# 		self.people = getPeople(filestream)	

def printPeople(people):
	for peep in people.people:
		print("Name: " + str(peep.name) + "\twith id: " 
			+ str(peep.personId))
	print("Number of people: " + str(peeprs.numPeople))

if __name__  == '__main__':
	peeprs = People("data.dinner")
	printPeople(peeprs)
