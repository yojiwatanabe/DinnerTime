from people 	import *
from random 	import randint

DINNERS_PER_WEEK	= 4
POSSIBLE_TIMES		= 5 
DINNER_DAYS			= ["Monday", "Tuesday", "Wednesday", "Thursday"]
DINNER_TIMES		= ["6:00", "6:30", "7:00", "7:30", "8:00"]

class WeekAnswer():
	dayAnswers 	= []
	people 		= []
	fitness 	= 0.0

	def __init__(self):
		self.people = People("data.dinner")
		self.createWeekAnswer()

	def createWeekAnswer(self):
		for i in range(DINNERS_PER_WEEK):
			answer = self.createSolution(self.people, DINNER_DAYS[i])
			self.dayAnswers.append(answer)

	def createSolution(self, people, day_id):
		dinnerTime	= randint(0, POSSIBLE_TIMES - 1)
		answer 		= DayAnswer(dinnerTime)
		answer.setFitness(people, day_id)
		return answer

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
			if (guest.availability[self.time] == "1"):
				temp += 1
				self.idList[guest.personId] = 1;
		self.fitness = (temp * 100) / guests.numPeople	