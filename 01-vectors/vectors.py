class Vector():
  def __init__(self, size):
    self.__elements = [None] * size
    self.__position = 0

  def insert_at(self, position, element):
    if (position >= 0) and (position < self.__position):
      initialVector = self.__elements[:position] + [None]
      finalVector = self.__elements[position:]
      self.__elements = initialVector + finalVector
      self.__elements[position] = element
      self.__position += 1
    else:
      print("Posição inválida")
    
  def insert_end(self, element):
    if self.__position >= self.__get_size():
      self.__elements = self.__elements + [None]
    
    self.__elements[self.__position] = element
    self.__position += 1
    
  def index(self, element):
    for i in range(self.__get_size()):
      if self.__elements[i] == element:
        return i
    return -1

  def contains(self, element):
    if self.index(element) == -1:
      return False
    else:
      return True

  def remove_at(self, position):
    initialVector = self.__elements[:position]
    finalVector = self.__elements[position+1:]
    self.__elements = initialVector + finalVector
    self.__position += -1

  def remove_element(self, element):
    index = self.index(element)

    if index != -1:
      self.remove_at(index)

  def __get_size(self):
    return len(self.__elements)

  def __str__(self):
    return ' '.join([str(i) for i in self.__elements])