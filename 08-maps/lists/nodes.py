class Node():
  def __init__(self, element, next = None):
    self.__element = element
    self.__next = next

  @property
  def element(self):
    return self.__element

  @element.setter
  def element(self, element):
    self.__element = element

  @property
  def next(self):
    return self.__next

  @next.setter
  def next(self, next):
    self.__next = next