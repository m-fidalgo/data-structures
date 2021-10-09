class Node():
  def __init__(self, element, next = None, previous = None):
    self.__element = element
    self.__next = next
    self.__previous = previous

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

  @property
  def previous(self):
    return self.__previous

  @previous.setter
  def previous(self, previous):
    self.__previous = previous