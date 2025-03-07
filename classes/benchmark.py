import sys
from classes.formatter import Formatter
from classes.randomArray import RandomArray
from classes.sorter import Sorter


class Benchmark:
  def __init__(self, functionRefs, ranges, metricsArray, recursionDepth=1000):
    self._recursionDepth = recursionDepth
    sys.setrecursionlimit(self._recursionDepth)
    self._sorterArray = []
    self._sorterOutput = dict()
    self.importedSorter = None
    self.numsArray = RandomArray(ranges["count"], ranges["lowRange"], ranges["highRange"]).array()
    for function in functionRefs:
      self.importedSorter = functionRefs[function]
      self._sorterArray.append(Sorter(self.importedSorter, ranges, function, self.numsArray))
      #self._sorterArray.append(Sorter(getattr(self.importedSorter, "sort"), ranges))
      
    for sorter in self._sorterArray:
       sorter.returnBenchmark()
       output = sorter.metrics.printMetrics()
       self._sorterOutput[output["algorithmName"]] = output
    self.formatter = Formatter(self._sorterOutput, metricsArray)

  @property
  def recursionDepth(self):
    return self._recursionDepth
  
  @recursionDepth.setter
  def recursionDepth(self, value):
    self._recursionDepth = value
    sys.setrecursionlimit(self._recursionDepth)