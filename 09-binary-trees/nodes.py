class Node():
  def __init__(self, value, left = None, right = None):
    self.__value = value
    self.__left = left
    self.right = right

  @property
  def value(self):
    return self.__value
  
  @property
  def left(self):
    return self.__left
  
  @left.setter
  def left(self, left):
    self.__left = left

  @property
  def right(self):
    return self.__right
  
  @right.setter
  def right(self, right):
    self.__right = right

  def weight(self):
    return self.__value

  def __str__(self):
    return ("[X]" if self.__left == None else f'[{self.__left.__str__()}]') + \
           (f'[{self.__value.__str__()}]') + \
           ("[X]" if self.__right == None else f'[{self.__right.__str__()}]')