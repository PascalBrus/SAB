import time
class colors:
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  
class Timestamp:
  def __init__(self):
    self.start()
  def start(self):
    self.startTime = time.time()
    self.endTime = 0
  def end(self):
    self.endTime = time.time()
    return (self.endTime - self.startTime)*1000*1000

class validateRanges:
  def __init__(self, ranges):
    self.ranges = ranges

  def validate(self) -> bool:
    if len(self.ranges) < 3:
      return False
    if self.ranges[1] >= self.ranges[2]:
      return False
    if self.ranges[0] <= 1:
      return False
    return True
