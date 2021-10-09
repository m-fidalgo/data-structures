from nodes import Node

class Queue():
  def __init__(self):
    self.__first = None
    self.__last = None
    self.__size = 0
  
  def insert(self, element):
    node = Node(element)
    if self.__is_empty():
      self.__first = node
      self.__last = node
    else:
      self.__last.next = node
      self.__last = node

    self.__size += 1

  def get_node(self, index):
    if not self.__is_empty() and index < self.__size:
      res = self.__first
      for i in range(index):
        res = res.next
      return res     

  def remove(self):
    if self.__is_empty():
      print("Fila vazia")
    else:
      next = self.__first.next
      self.__first = None
      self.__first = next
      self.__size += -1

  def __is_empty(self):
    return self.__size == 0

  def __str__(self):
    if self.__is_empty():
      return "Fila vazia"
    
    temp = self.__first
    ret = 'início'

    while temp:
      ret = f"{ret} > {temp.element}"
      temp = temp.next

    ret = f"{ret} > fim"
    return ret