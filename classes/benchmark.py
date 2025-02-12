import sys
from classes.formatter import Formatter
from classes.sorter import Sorter


class Benchmark:
  def __init__(self, options, ranges, recursionDepth=1000):
    self._recursionDepth = recursionDepth
    self._sorterArray = []
    self._sorterOutput = []
    self.importedSorter = None
    sys.setrecursionlimit(self._recursionDepth)
    for option in options:
      self.importedSorter = self.importSorter(option)
      self._sorterArray.append(Sorter(self.importedSorter.sort, ranges, option))
      #self._sorterArray.append(Sorter(getattr(self.importedSorter, "sort"), ranges))
      
    for sorter in self._sorterArray:
       self._sorterOutput.append(sorter.returnBenchmark())
       self._sorterOutput.append(sorter.metrics.printMetrics())
    self.formatter = Formatter(self._sorterOutput)

  @property
  def recursionDepth(self):
    return self._recursionDepth
  
  @recursionDepth.setter
  def recursionDepth(self, value):
    self._recursionDepth = value
    sys.setrecursionlimit(self._recursionDepth)

  def importSorter(self, option):
    moduleName = "functions."+option
    #print(option)
    return __import__(moduleName, fromlist=["sort"])

def sortBubble(nums):
    swapping = True
    end = len(nums)
    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                temp = nums[i - 1]
                nums[i - 1] = nums[i]
                nums[i] = temp
                swapping = True
        end -= 1
    return nums
