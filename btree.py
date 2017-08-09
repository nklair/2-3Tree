from node import Node
from node import RootNode

class BTree:
  def __init__(self, nodeSize):
    self.nodeSize = nodeSize
    self.root = RootNode(self.nodeSize)
    
  def insert(self, value):
    if self.root.child == None:
      self.root.insert(value)
    else:
      insertRec(self.root.child, value)

  def insertRec(self, node, value):
    if value in node.values:
      return
    else:
      child = 0
      while child < len(node.values) and node.values[child] > value:
          child = child + 1
      if node.children[child] == None:
        node.insert(value)
      else:
        insertRec(node.children[child], value)
  
  def inOrderTraversal(self, function):
    recInOrder(function, self.root)

  def recInOrder(self, function, node):
    if node == None:
      return
    
     
