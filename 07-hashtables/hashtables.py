from lists.lists import List

class HashTable():
  def __init__(self):
    self.__elements = List()
    self.__categories = 10
    self.__size = 0

    for i in range(self.__categories):
      self.__elements.insert(List())

  def __generate_hash_number(self, element):
    return hash(element) % self.__categories

  def contains(self, element):
    hash_number = self.__generate_hash_number(element)
    category = self.__elements.get_node_element(hash_number)
    return category.contains(element)

  def insert(self, element):
    if self.contains(element):
      return False
    hash_number = self.__generate_hash_number(element)
    category = self.__elements.get_node_element(hash_number)
    category.insert(element)
    self.__size += 1
    return True

  def remove(self, element):
    if not self.contains(element):
      return False
    hash_number = self.__generate_hash_number(element)
    category = self.__elements.get_node_element(hash_number)
    category.remove_element(element)
    return True

  def __str__(self):
    return self.__elements.__str__()