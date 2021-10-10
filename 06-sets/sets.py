from nodes import Node

class Set:
  def __init__(self):
    self.__first_node = None
    self.__last_node = None
    self.__size = 0

  def index(self, element):
    for i in range(self.__size):
      node = self.get_node(i)
      if node.element == element:
        return i
    return -1

  def contains(self, element):
    if self.index(element) == -1:
      return False
    return True 

  def __is_empty(self):
    return self.__size == 0
  
  def insert(self, element):
    node = Node(element)
    if self.contains(element):
      print("Elemento já inserido")
    else:
      if self.__is_empty():
        self.__first_node = node
        self.__last_node = node
      else:
        self.__last_node.next = node
        self.__last_node = node

      self.__size += 1
  
  def insert_at(self, index, element):
    node = Node(element)
    if self.contains(element):
      print("Elemento já inserido")
      return
    elif index > self.__size or index < 0:
      print("Posição inválida")
      return
    elif index == 0:
      node.next = self.__first_node
      self.__first_node = node
    elif index == self.__size:
      self.__last_node.next = node
      self.__last_node = node
    else:
      prev = self.get_node(index - 1)
      current = self.get_node(index)
      prev.next = node
      node.next = current

    self.__size += 1

  def get_node(self, index):
    if not self.__is_empty() and index < self.__size:
      res = self.__first_node
      for i in range(index):
        res = res.next
      return res  
  
  def remove_at(self, index):
    if index > self.__size or index < 0:
      print("Posição inválida")
      return
    elif index == 0:
      next = self.__first_node.next
      self.__first_node = None
      self.__first_node = next
    elif index == self.__size - 1:
      prev = self.get_node(self.__size - 2)
      prev.next = None
      self.__last_node = prev
    else:
      remove = self.get_node(index)
      prev = self.get_node(index - 1)
      prev.next = remove.next
      remove.next = None

    self.__size += -1

  def remove_element(self, element):
    self.remove_at(self.index(element))
  
  def __str__(self):
    if self.__is_empty():
      return "Set vazio"
    
    temp = self.__first_node
    ret = 'início'

    while temp:
      ret = f"{ret} > {temp.element}"
      temp = temp.next

    ret = f"{ret} > fim"
    return ret
