from classes.misc import Timestamp


class Metrics:
  def __init__(self, nums):
    self._timeStamp = Timestamp()
    self.duration = 0
    self.iteration = 0
    self.recursions = 0
    self.assignments = 0
    self.elementCount = nums.length()
  
  def tickIteration(self):
    self.iteration += 1
  def tickRecursion(self):
    self.recursions += 1
  def tickAssignments(self):
    self.assignments += 1
  def startTimer(self):
    self._timeStamp.start()
  def endTimer(self):
    self.duration = self._timeStamp.end()
    return self.duration
