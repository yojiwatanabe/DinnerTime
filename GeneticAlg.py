# -*- coding: utf-8 -*-

"""
Genetic Algorithm functions
GeneticAlg.py

Defines Genetic Algorithm functions for Dinner time optimizer using a simple 
modified genetic annealing algorithm.
"""
from packSolution 	import *
from math 			import ceil

POPULATION_SIZE 	= 1000
VARIATION_FACTOR 	= 0.2

def passGeneration(solutions):
	solutions		= rankSolutions(solutions)
	variateDNA(solutions)

	return solutions

def getSolutions(num):
	weekSolution = [0] * num
	for i in range(num):
		weekSolution[i] = WeekAnswer()
	return weekSolution

def rankSolutions(solutions):
	fitness = [0] * len(solutions)
	for i in range(len(solutions)):
		fitness[i] = unpackFitness(solutions[i])

	return [x for _,x in sorted(zip(fitness, solutions), reverse = True)]

def variateDNA(solutions):
	numNewDNA 	= int(ceil(len(solutions) * VARIATION_FACTOR))
	newDNA 		= getSolutions(numNewDNA)
	packedDNA 	= packSolutions(newDNA, numNewDNA)

	for i in range(numNewDNA):
		solutions[len(solutions) - i - 1] = packedDNA[i]

	return