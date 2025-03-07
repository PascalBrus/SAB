from classes.metrics import Metrics
from classes.randomArray import RandomArray
from config import LOOP
import progressbar
import sys, os


class Sorter: 
  #metadata for sorting functions like what to track for them, like recursions for quick sort but doesnt make sense for bubble???
  #sorterFN the Sorter Function
  #ranged Dict with randomArray ranges 
  def __init__(self, sorterFN, ranges, option, numsArray=[]):
     self._ranges = ranges
     if(numsArray == []):
      #print("its so over")
      self._randomArray = RandomArray(self._ranges["count"], self._ranges["lowRange"], self._ranges["highRange"])
      self._nums = self._randomArray.array()
     else:
       #print("yippie!")
       #print(numsArray)
       self._nums = numsArray
     self._fn = sorterFN
     self.metrics = Metrics(self.nums, option, self._ranges)
     self.sortedNumsRef = sorted(self._nums)


  @property
  def nums(self):
    return self._nums.copy()
  def _runAlgorithms(self):
      for x in progressbar.progressbar(range(0,LOOP)):
        self.metrics.startTimer()
        sorted = self._fn.sort(self.nums, self.metrics)
        self.metrics.endTimer()

        if (sorted != self.sortedNumsRef):
          os.system('clear')
          print("SORTING FAILED CHECK THIS ALGORITHM: " + str(self._fn))
          sys.exit()
        self.metrics.addSortedNums(sorted)
      return sorted, self.metrics.normalizedDuration

  def returnBenchmark(self):
    return self._runAlgorithms()
  
  