# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# People Object
# Takes in a filename, gets information and initializes Person class for each
# instance of a Person in the data file
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
class People():
	numPeople 	= 0
	people 		= []

	def __init__(self, filename):
		self.getPeople(filename)

	def getPeople(self, filename):
		f 		= open(filename)
		arr 	= []

		for i, j in enumerate(f): arr.append(j)
		self.numPeople 	= i + 1
		self.people		= [0] * (self.numPeople)

		for j in range(i + 1):
			self.people[j] = Person(arr[j], j)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Person Object
# Takes in a full line from a people file, gets information and sets it
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
class Person():
	personId		= 0
	name 			= ""
	availability 	= []

	def __init__(self, line, pid):
		self.setName(line)
		self.setAvailability(line)
		self.setId(pid)

	def setName(self, line):
		words 				= line.split()
		self.name 			= words[0]

	def setAvailability(self, line):
		words 				= line.split()
		self.availability 	= words[1]

	def setId(self, pid):
		self.personId 		= pid