from people 	import *
from random 	import randint

DINNERS_PER_WEEK	= 4
POSSIBLE_TIMES		= 5 
DINNER_DAYS			= ["Monday", "Tuesday", "Wednesday", "Thursday"]
DINNER_TIMES		= ["6:00", "6:30", "7:00", "7:30", "8:00"]

class WeekAnswer():
	dayAnswers 	= []
	guests 		= []
	fitness 	= 0.0

	def __init__(self):
		self.guests = People("data.dinner")
		self.createWeekAnswer()
		self.calculateFitness()
		self.variabilityFitness()

	def createWeekAnswer(self):
		for i in range(DINNERS_PER_WEEK):
			answer = self.createSolution(self.guests, i)
			self.dayAnswers.append(answer)

	def createSolution(self, people, day_id):
		dinnerTime	= randint(0, POSSIBLE_TIMES - 1)
		answer 		= DayAnswer(dinnerTime)
		answer.setFitness(people, day_id)
		return answer

	def calculateFitness(self):
		for day in range(DINNERS_PER_WEEK):
			self.fitness += self.dayAnswers[day].fitness
		self.fitness 	= self.fitness / DINNERS_PER_WEEK

	def variabilityFitness(self):
		variability = []
		for guest in self.guests.people:
			variability.append(0)
			for i in range(DINNERS_PER_WEEK):
				if self.dayAnswers[i].idList[guest.personId] == 1:
					variability[guest.personId] += 1
		attendanceDifference 	= max(variability) - min(variability)
		var 			= 1 - 1.0/(attendanceDifference * attendanceDifference)
		if var == 0: var = 1
		self.fitness 	= self.fitness * var

		print("attDiff = %i\t and var = %.4f" % (attendanceDifference, var))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Answer Object
# Takes in a full line from a people file, gets information and sets it
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
class DayAnswer():
	time 	= 0
	fitness	= 0
	idList  = []

	def __init__(self, time):
		self.setTime(time)

	def setTime(self, time):
		self.time 	= time

	def setFitness(self, guests, day_id):
		temp 		= 0.0
		self.idList = [0] * guests.numPeople
		for guest in guests.people:
			if (guest.availability[self.time + day_id * POSSIBLE_TIMES] == "1"):
				temp += 1
				self.idList[guest.personId] = 1;
		self.fitness = (temp * 100) / guests.numPeople	