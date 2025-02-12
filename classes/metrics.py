from classes.misc import Timestamp
from config import DEVIATION, LOOP, ROUNDING


class Metrics:
  def __init__(self, nums):
    self._timeStamp = Timestamp()
    self._normalizedDuration = 0
    self.iteration = 0
    self.recursions = 0
    self.assignments = 0
    self.elementCount = len(nums)
    self.durationArray = []
    self.normalizedDurationArray = []
  
  def tickIteration(self):
    self.iteration += 1
  def tickRecursion(self):
    self.recursions += 1
  def tickAssignments(self):
    self.assignments += 1
  def startTimer(self):
    self._timeStamp.start()

  def endTimer(self):
    end = self._timeStamp.end()
    self.durationArray.append(end)
    return end
  
  @property
  def normalizedDuration(self):
    self._normalizedDuration = round(sum(self.normalizeTimes())/float(LOOP-(2*DEVIATION)),ROUNDING)
    return self._normalizedDuration

  def normalizeTimes(self):
     array = self.durationArray.copy()
     for x in range(0, DEVIATION):
      #print("min: "+ str(array.index(min(self.durationArray))))
      #print("max: "+ str(array.index(max(self.durationArray))))
      #print("Normalized Array BEFORE pop: " + str(array))
      array.pop(array.index(min(array))-1)
      array.pop(array.index(max(array))-1)
      #print("Normalized Array AFTER pop: " + str(array))
     self.normalizedDurationArray = array
     return array
  
  def printMetrics(self):
    return {"normalizedDuration": self._normalizedDuration,
            "durationArray": self.durationArray,
            "normalizedDurationArray:": self.normalizedDurationArray,
            "iterations": self.iteration,
            "recursions": self.recursions,
            "assignments": self.assignments,
            "elementCount": self.elementCount}
