


class Node:
	def __init__(self, size, parent):
		self.maxSize = size
		self.values = []
		self.children = []
		i = 0
		while i < self.maxSize / 2:
			self.children.append(None)
			i += 1
		self.parent = parent

	def insert(self, value, newChild=None):
		valIndex = 0
		while valIndex < len(self.values):
			if self.values[valIndex] > value:
				break
			valIndex += 1
		self.values.insert(valIndex, value)
		if newChild == None:
			self.children.append(newChild)
		else:
			newChildValue = newChild.getValues()[0]
			valIndex = 0
			while valIndex < len(self.values):
				if self.values[valIndex] > newChildValue:
					break
				valIndex += 1
			self.children.insert(valIndex, newChild)

		if len(self.values) >= self.maxSize:
			self.promote()

	def promote(self):
		pass

	def getValues(self):
		pass


