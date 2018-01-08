from people 	import *
from random		import randint, seed
import sys

DINNERS_PER_WEEK	= 4
POSSIBLE_TIMES		= 5 
DINNER_DAYS			= ["Monday", "Tuesday", "Wednesday", "Thursday"]
DINNER_TIMES		= ["6:00", "6:30", "7:00", "7:30", "8:00"]

class WeekAnswer():
	dayAnswers 		= []
	guests 			= []
	guestAttendance = []
	fitness 		= 0.0

	def __init__(self):
		self.guests = People("data.dinner")
		self.createWeekAnswer()
		# sys.stderr.write(str(self.dayAnswers[0].time))
		self.calculateFitness()
		self.variabilityFitness()

	def createWeekAnswer(self):
		week = [0] * DINNERS_PER_WEEK
		for i in range(DINNERS_PER_WEEK):
			answer = self.createSolution(self.guests, i)
			week[i] = answer
		self.dayAnswers = week

	def createSolution(self, people, day_id):
		dinnerTime	= randint(0, POSSIBLE_TIMES - 1)
		answer 		= DayAnswer(dinnerTime)
		answer.setFitness(people, day_id)
		print DINNER_DAYS[day_id] + " " + str(DINNER_TIMES[answer.time])
		return answer

	def calculateFitness(self):
		for day in range(DINNERS_PER_WEEK):
			self.fitness += self.dayAnswers[day].fitness
		self.fitness 	= self.fitness / DINNERS_PER_WEEK

	def variabilityFitness(self):
		self.guestAttendance = [0] * self.guests.numPeople
		for j in range(self.guests.numPeople):
			for i in range(DINNERS_PER_WEEK):
				if self.dayAnswers[i].idList[self.guests.people[j].personId] == 1:
					self.guestAttendance[self.guests.people[j].personId] += 1
		
		attDiff 		= max(self.guestAttendance) - min(self.guestAttendance)
		if 	 attDiff == 0 : var = 1
		elif attDiff == 1 : var = 0.995
		else: 	var 	= ((1.0/(attDiff * attDiff)) / 4) + 0.75
		
		# print("%.3f * (%.3f / 2)" % (self.fitness, var))
		# print "pre_fit = " + str(self.fitness),
		# print self.guestAttendance
		self.fitness 			= self.fitness * var
		# print "\tpost fit = " + str(self.fitness)

		# print("attDiff = %i\t and var = %.3f" % (attDiff , var))
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