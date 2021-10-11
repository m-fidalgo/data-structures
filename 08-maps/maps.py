from lists.lists import List
from association import Association

class Map():
  def __init__(self):
    self.__elements = List()
    self.__categories = 10

    for i in range(self.__categories):
      self.__elements.insert(List())

  def __generate_hash_number(self, key):
    return hash(key) % self.__categories

  def contains_key(self, key):
    hash_number = self.__generate_hash_number(key)
    category = self.__elements.get_node_element(hash_number)
    for i in range (category.size):
      association = category.get_node_element(i)
      if association.key == key:
        return True
    return False

  def remove(self, key):
    hash_number = self.__generate_hash_number(key)
    category = self.__elements.get_node_element(hash_number)
    for i in range (category.size):
      association = category.get_node_element(i)
      if association.key == key:
        category.remove_element(association)
        return True
    return False

  def insert(self, key, value):
    if self.contains_key(key):
      self.remove(key)
    hash_number = self.__generate_hash_number(key)
    category = self.__elements.get_node_element(hash_number)
    category.insert(Association(key, value))
  
  def get_element(self, key):
    hash_number = self.__generate_hash_number(key)
    category = self.__elements.get_node_element(hash_number)
    for i in range(category.size):
      association = category.get_node_element(i)
      if association.key == key:
        return association.value
    return False

  def __str__(self):
    return self.__elements.__str__()