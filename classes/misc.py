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


class validateArgs:
  def __init__(self, ogArgs, args):
    self.ogArgs = set(ogArgs)
    self.args = args
  
  def validate(self) -> bool:
    for arg in self.args:
      if arg not in self.ogArgs:
        return False
    return True


