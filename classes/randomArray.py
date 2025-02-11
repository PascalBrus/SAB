import random


class RandomArray:
  def __init__(self, count, lowRange, highRange):
    self._count = count
    self._lowRange = lowRange
    self._highRange = highRange

  @property
  def count(self):
    return self._count
  
  @count.setter
  def count(self, value):
    self._count = value

  @property
  def lowRange(self):
    return self._lowRange
  
  @lowRange.setter
  def lowRange(self, value):
    self._lowRange = value

  @property
  def highRange(self):
    return self._highRange

  @highRange.setter
  def highRange(self, value):
    self._highRange = value


  def array(self):
    return self.__createArray()

  def __createArray(self):
    arr = []
    for x in range(0, self.count):
      arr.append(random.randint(self.lowRange, self.highRange))
    return arr
  