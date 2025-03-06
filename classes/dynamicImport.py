from importlib import import_module
import os

class DynamicImport:
  def __init__(self, source="functions"):
    self.SorterFunctionNames = self.getSorterFunctionNames()
    self.SorterFunctions = self.runImport()

  def returnImport(self):
    return self.SorterFunctionNames, self.SorterFunctions
  
  def getSorterFunctionNames(self):
    files = [f for f in os.listdir("functions") if os.path.isfile("functions/"+f)]
    sortingOptionNames = []
    for file in files:
      sortingOptionNames.append(file[:-3])
    return sortingOptionNames

  def runImport(self):
    imports = []
    for function in self.SorterFunctionNames:
      imports.append(import_module("functions."+ function))
    return imports
  
  def filterRefs(self):
    pass