# -*- coding: utf-8 -*-

"""
Genetic Algorithm functions
GeneticAlg.py

Defines Genetic Algorithm functions for Dinner time optimizer using a simple 
modified genetic annealing algorithm.
"""
from packSolution 	import *

def rankSolutions(solutions):
	fitness = [0] * len(solutions)
	for i in range(len(solutions)):
		fitness[i] = unpackFitness(solutions[i])

	return [x for _,x in sorted(zip(fitness, solutions), reverse = True)]