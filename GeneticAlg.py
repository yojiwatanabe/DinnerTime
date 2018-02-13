# -*- coding: utf-8 -*-

"""
Genetic Algorithm functions
GeneticAlg.py

Defines Genetic Algorithm functions for Dinner time optimizer using a simple 
modified genetic annealing algorithm.
"""
import sys
from packSolution 	import *
from math 			import ceil, floor

INIT_GEN 			= 0
END_GEN  			= 10
POPULATION_SIZE 	= 1000
PERFECT_SCORE 		= 100.0
NUM_ANSWERS 		= 10
CULL_RATIO		 	= 0.8

#					startCycle()
#
# Begins a new population of WeekAnswers to put through the genetic algorithm.
# Generates solutions, packs them, and begins passing through each generation,
# applying the given mutations and crossovers.
def startCycle():
	rawSolutions 	= getSolutions(POPULATION_SIZE)
	packedSolutions = packSolutions(rawSolutions, POPULATION_SIZE)
	gen  			= INIT_GEN

	while (stopConditionsMet(gen, packedSolutions) == False):
		passGeneration(packedSolutions)
		gen += 1

	return getNBestAnswers(NUM_ANSWERS, packedSolutions)

def stopConditionsMet(gen, words):
	if (gen > END_GEN):
		print "Reached end generation"
		return True
	elif (unpackFitness(words[0]) == PERFECT_SCORE):
		print "Perfect score!"
		return True
	return False

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
	fitness = [0] * (POPULATION_SIZE)
	for i in range(POPULATION_SIZE):
		fitness[i] = unpackFitness(solutions[i])

	sortedSols = [x for _,x in sorted(zip(fitness, solutions), reverse = True)]
	return sortedSols

def variateDNA(solutions):
	numNewDNA 	= int(ceil(POPULATION_SIZE * (1 - CULL_RATIO)))
	newDNA 		= getSolutions(numNewDNA)
	packedDNA 	= packSolutions(newDNA, numNewDNA)

	for i in range(numNewDNA):
		solutions[POPULATION_SIZE - i - 1] = packedDNA[i]

	return

def getNBestAnswers(numAnswers, solutions):
	solutions = rankSolutions(solutions)
	toReturn = [0] * numAnswers

	for i in range(numAnswers):
		toReturn[i] = unpackSolution(solutions[i])

	return toReturn
