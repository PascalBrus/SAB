import sys
from classes.formatter import Formatter
from classes.randomArray import RandomArray
from classes.sorter import Sorter


class Benchmark:
  def __init__(self, options, ranges, metricsArray=[], recursionDepth=1000):
    self._recursionDepth = recursionDepth
    self._sorterArray = []
    self._sorterOutput = dict()
    self.importedSorter = None
    sys.setrecursionlimit(self._recursionDepth)
    self.numsArray = RandomArray(ranges["count"], ranges["lowRange"], ranges["highRange"]).array()
    for option in options:
      self.importedSorter = self.importSorter(option)
      self._sorterArray.append(Sorter(self.importedSorter.sort, ranges, option, self.numsArray))
      #self._sorterArray.append(Sorter(getattr(self.importedSorter, "sort"), ranges))
      
    for sorter in self._sorterArray:
       sorter.returnBenchmark()
       self._sorterOutput.append(sorter.metrics.printMetrics())
    self.formatter = Formatter(self._sorterOutput, metricsArray)

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
