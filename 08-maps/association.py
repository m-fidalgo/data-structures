class Association():
  def __init__(self, key, value):
    self.__key = key
    self.__value = value

  @property
  def key(self):
    return self.__key

  @property
  def value(self):
    return self.__value

  def __str__(self):
    return f"{self.__key} {self.__value}"