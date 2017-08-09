class Node:
	def __init__(self, size, parent):
		self.maxSize = size
		self.values = []
		self.children = []
		i = 0
		while i <= self.maxSize:
			self.children.append(None)
			i += 1
		self.parent = parent

	def insert(self, value, leftChild=None, rightChild=None):
		valIndex = 0
		while valIndex < len(self.values):
			if self.values[valIndex] > value:
				break
			valIndex += 1
		self.values.insert(valIndex, value)
		# Make sure the children know their parent
		if leftChild != None:
			leftChild.parent = self
		if rightChild != None:
			rightChild.parent = self
		# Left needs to replace old child
		self.children[valIndex] =  leftChild
		#right needs to be inserted in children list
		self.children.insert(valIndex + 1,rightChild)
		self.children.pop()

		if len(self.values) >= self.maxSize:
			self.promote()

	def promote(self):
		indToPromote = int(self.maxSize / 2)
		val = self.values[indToPromote]
		# Don't know who the new children's parent will be yet
		rightChild = Node(self.maxSize, None)
		leftChild = Node(self.maxSize, None)
		i = 0
		while i < len(self.values):
			if(i < indToPromote):
				leftChild.insert(self.values[i], self.children[i], self.children[i + 1])
			if(i > indToPromote):
				rightChild.insert(self.values[i], self.children[i], self.children[i + 1])
			i += 1

		self.parent.insert(val, leftChild, rightChild)

	def print(self):
		print(str(self.values))
		print(str(self.children))
		for child in self.children:
			if(child != None):
				print(child.print())

# Node to handle the case when a new node needs to be created as the root
class RootNode:
	def __init__(self, size):
		self.child = None
		self.maxSize = size

	def insert(self, value, leftChild=None, rightChild=None):
		newRoot = Node(self.maxSize, self)
		# Make sure the children know their parent
		if leftChild != None:
			leftChild.parent = newRoot
		if rightChild != None:
			rightChild.parent = newRoot
		newRoot.insert(value, leftChild, rightChild)
		self.child = newRoot

	def print(self):
		if(self.child != None):
			self.child.print()




