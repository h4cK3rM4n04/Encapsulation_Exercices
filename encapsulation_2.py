#coding:utf-8

class Personne:

	"""docstring for Personne"""

	def __init__(self, last_name, first_name, age, size):

		self._last_name = last_name
		self._first_name = first_name
		self._age = age
		self._size = size

	def description(self):
		return str(self._last_name) + " " + str(self._first_name) + " " + str(self._age) + " " + str(self._size)

	def _GetCompleteName(self):
		return self._last_name + " " + self._first_name
	nom_complet = property(_GetCompleteName)


if __name__ == "__main__":
	p1 = Personne("M4n04", "h4cK3r", 16, 170)
	print(p1.description())
	print(p1.nom_complet)