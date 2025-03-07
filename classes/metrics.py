from classes.misc import Timestamp
from config import OUTLIERS, LOOP, ROUNDING


class Metrics:
  def __init__(self, nums, option, ranges):
    self._timeStamp = Timestamp()
    self.nonNormalizedDuration = 0
    self._normalizedDuration = 0
    self.iteration = 0
    self.recursions = 0
    self.assignments = 0
    self.durationArray = []
    self.normalizedDurationArray = []
    self.algorithmName = option
    self.origionalNums = nums
    self.sortedNums = []
    self.ranges = ranges
  
  def tickIteration(self):
    self.iteration += 1
  def tickRecursion(self):
    self.recursions += 1
  def tickAssignment(self):
    self.assignments += 1
  def startTimer(self):
    self._timeStamp.start()
  def addSortedNums(self, value):
    self.sortedNums = value

  def endTimer(self):
    end = self._timeStamp.end()
    self.durationArray.append(end)
    return end
  
  @property
  def normalizedDuration(self):
    self._normalizedDuration = round(sum(self.normalizeTimes())/float(LOOP-(2*OUTLIERS)),ROUNDING)
    self.nonNormalizedDuration = sum(self.durationArray)/float(LOOP)
    return self._normalizedDuration

  def normalizeTimes(self):
     array = self.durationArray.copy()
     for x in range(0, OUTLIERS):
      array.pop(array.index(min(array))-1)
      array.pop(array.index(max(array))-1)
     self.normalizedDurationArray = array
     return array
  
  def printMetrics(self):
    return {"algorithmName": self.algorithmName.capitalize(),
            "durationArray": self.durationArray,
            "nonNormalizedDuration": self.nonNormalizedDuration,
            "normalizedDurationArray": self.normalizedDurationArray,
            "normalizedDuration": self._normalizedDuration,
            "iterations": self.iteration,
            "recursions": self.recursions,
            "assignments": self.assignments,
            "numberRange": f"{self.ranges['lowRange']} : {self.ranges['highRange']}",
            "elementCount": self.ranges["count"],
            "loopCount": LOOP,
            "outliers": OUTLIERS,
            "origionalNums": self.origionalNums,
            "sortedNums": self.sortedNums
            }
