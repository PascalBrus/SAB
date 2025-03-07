from importlib import import_module
import os

class DynamicImport:
  def __init__(self, source="functions"):
    self.sorterFunctions = self.getSorterFunctionNames()
    #self.SorterFunctions = self.runImport()

  def returnImport(self):
    return self.sorterFunctions
  
  def getSorterFunctionNames(self):
    files = [f for f in os.listdir("functions") if os.path.isfile("functions/"+f)]
    sortingOptionNames = dict()
    for file in files:
      sortingOptionNames[file[:-3]] = self.runImport(file[:-3])
    return sortingOptionNames

  def runImport(self, function):
    return import_module("functions."+ function)
  
  def filterFunctionRefs(self, sorterFunctions, filters):
    for function in list(sorterFunctions):
      if function not in filters:
        sorterFunctions.pop(function)
    return sorterFunctions
      