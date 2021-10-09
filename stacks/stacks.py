from nodes import Node

class Stack():
  def __init__(self):
    self.__bottom = None
    self.__top = None
    self.__size = 0
  
  def push(self, element):
    node = Node(element)
    if self.__is_empty():
      self.__bottom = node
      self.__top = node
    else:
      self.__top.next = node
      self.__top = node

    self.__size += 1

  def get_node(self, index):
    if not self.__is_empty() and index < self.__size:
      res = self.__bottom
      for i in range(index):
        res = res.next
      return res     

  def pop(self):
    if self.__is_empty():
      print("Pilha vazia")
    else:
      prev = self.get_node(self.__size - 2)
      prev.next = None
      self.__top = prev

    self.__size += -1

  def __is_empty(self):
    return self.__size == 0

  def __str__(self):
    if self.__is_empty():
      return "Pilha vazia"
    
    temp = self.__bottom
    ret = 'início'

    while temp:
      ret = f"{ret} > {temp.element}"
      temp = temp.next

    ret = f"{ret} > topo"
    return ret