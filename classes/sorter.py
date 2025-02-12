from classes.metrics import Metrics
from classes.randomArray import RandomArray
from config import DEVIATION, LOOP, ROUNDING


class Sorter: 
  #metadata for sorting functions like what to track for them, like recursions for quick sort but doesnt make sense for bubble???
  #sorterFN the Sorter Function
  #ranged Dict with randomArray ranges 
  def __init__(self, sorterFN, ranges):
     self._ranges = ranges
     self._randomArray = RandomArray(self._ranges["count"], self._ranges["lowRange"], self._ranges["highRange"])
     self._nums = self._randomArray.array()
     self._fn = sorterFN
     self.metrics = Metrics(self.nums)


  @property
  def nums(self):
    return self._nums.copy()
  def _runAlgorithms(self):
      times = []
      for x in range(0,LOOP):
        self.metrics.startTimer()
        sorted = self._fn(self.nums, self.metrics)
        end = self.metrics.endTimer()
        times.append(end)
      self.standartAbweichung(times)
      return sorted, round(sum(times)/float(LOOP-2*DEVIATION),ROUNDING)
  
  def standartAbweichung(self, times):
     for x in range(0, DEVIATION):
      times.pop(times.index(min(times)))
      times.pop(times.index(max(times)))
     return times

  def returnBenchmark(self):
    return self._runAlgorithms()
  
  