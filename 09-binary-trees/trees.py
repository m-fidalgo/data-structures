from nodes import Node

class Tree():
  def __init__(self, root = None):
    self.__root = root
  
  @property
  def root(self):
    return self.__root
  
  def insert(self, value):
    node = Node(value)

    if self.__root == None:
      self.__root = node
    else:
      self.__insert_node(self.__root, node)

  def __insert_node(self, ref, node):
    if ref.value < node.value:
      if ref.right is None:
        ref.right = node
      else:
        self.__insert_node(ref.right, node)
    else:
      if ref.left is None:
        ref.left = node
      else:
        self.__insert_node(ref.left, node)

  def get(self, value):
    try:
      self.__get_node(self.__root, Node(value))
      return True
    except ValueError as e:
      print(e)
      return False

  def __get_node(self, ref, node):
    if ref is None:
      raise ValueError("Não Encontrado")
    elif ref.value == node.value:
      return ref
    elif ref.value < node.value:
      self.__get_node(ref.right, node)
    else:
      self.__get_node(ref.left, node)

  def print_erd(self, ref): #em ordem
    if ref != None:
      self.print_erd(ref.left)
      print(ref.value.__str__())
      self.print_erd(ref.right)
    return

  def print_red(self, ref): #pré ordem
    if ref != None:
      print(ref.value.__str__())
      self.print_red(ref.left)
      self.print_red(ref.right)
    return 

  def print_edr(self, ref): #pós ordem
    if ref != None:
      self.print_edr(ref.left)
      self.print_edr(ref.right)
      print(ref.value.__str__())
    return 

  def height(self, ref):
    if ref == None:
      return -1
    left_height = self.height(ref.left)
    right_height = self.height(ref.right)
    return (left_height + 1) if left_height > right_height else (right_height + 1)

  def __str__(self):
    return ("[X]" if self.__root == None else self.__root.__str__())