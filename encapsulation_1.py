#coding:utf-8
class Humain:

	def __init__(self, nom, age):

		self._nom = nom
		self._age = age


	def _getAge(self):
		return self._age

	def _setAge(self, nouvel):
		self._age = nouvel

	def _getName(self):
		return self._nom

	def _setName(self, nName):
		self._nom = nName


	#getter setter deleter helper
	variable_x = property(_getAge, _setAge,)

	def _getName(self):
		return self._nom

	def _setName(self, nName):
		self._nom = nName

	var = property(_getName, _setName)




#Programme principal
h1 = Humain("h4cK3rM4n04", 26)
h1.variable_x = 14
print(h1.variable_x)

h1.var = h1.var[::-1]
print(h1.var + "\n")


'''h1.variable_quelconque = 14
print(h1.variable_quelconque)'''