import os
from classes.misc import colors


class Formatter:
  def __init__(self, nums=[], mode="PRINT"):
    self._nums = nums
    self.output = ""
    self.mode = mode

  def printState(self):
    #for debugging removed
    os.system('clear')

    


    myMin = min(times)
    myMax = max(times)
    self.output = self.output.replace(" "+str(myMin)+"µs", (f" {colors.OKGREEN}{myMin}µs{colors.ENDC}"))
    self.output = self.output.replace(" "+str(myMax)+"µs", (f" {colors.FAIL}{myMax}µs{colors.ENDC}"))
    print(self.output)