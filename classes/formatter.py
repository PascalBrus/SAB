import os
from classes.misc import colors
from rich.console import Console
from rich.table import Table
from rich import print

# metricsArray: Literal["minimal", "default", "extended", "all"] = ["default"]

class Formatter:
  def __init__(self, sorterOutput, metricOption):
    self._metricOption = metricOption
    self._metricOptionArray = self.createMetricOptions()
    self.console = Console()
    # for element in sorterOutput:
    #    if isinstance(element, dict):
    #     for subelement, value in element.items():
    #       print(f"{subelement}: {value}")
    # print("\n\n")
    self.table = Table(show_header=True, header_style="bold green")
    self.formatMetrics(sorterOutput)

  def createTableColumns(self):
    #adds columns to table
    for metrics in self._metricOptionArray.values():
      self.table.add_column(metrics)

  def createTableRows(self, sorterOutput):
    for key in sorterOutput.keys():
      #print(self._metricOption)
      if(self._metricOption == "minimal"):
       #print("minimal")
       self.table.add_row(sorterOutput[key]["algorithmName"], 
                      str(sorterOutput[key]["normalizedDuration"]))
      if(self._metricOption == "default"):
        #print("default")
        self.table.add_row(sorterOutput[key]["algorithmName"],
                      str(sorterOutput[key]["normalizedDuration"]),
                      str(sorterOutput[key]["iterations"]),
                      str(sorterOutput[key]["recursions"]),
                      str(sorterOutput[key]["assignments"]))
      if(self._metricOption == "extended"):
          #print("extended")
          self.table.add_row(sorterOutput[key]["algorithmName"],
                      str(sorterOutput[key]["normalizedDuration"]),
                      str(sorterOutput[key]["nonNormalizedDuration"]),
                      str(sorterOutput[key]["iterations"]),
                      str(sorterOutput[key]["recursions"]),
                      str(sorterOutput[key]["assignments"]))
      if(self._metricOption == "alev"):
        #print("alev")
        self.table.add_row(sorterOutput[key]["algorithmName"],
                      str(sorterOutput[key]["normalizedDuration"]),
                      str(sorterOutput[key]["nonNormalizedDuration"]),
                      str(sorterOutput[key]["iterations"]),
                      str(sorterOutput[key]["recursions"]),
                      str(sorterOutput[key]["assignments"]),
                      str(sorterOutput[key]["durationArray"]),
                      str(sorterOutput[key]["normalizedDurationArray"]))
      if(self._metricOption == "all"):
        #print("all")
        self.table.add_row(sorterOutput[key]["algorithmName"],
                      str(sorterOutput[key]["normalizedDuration"]),
                      str(sorterOutput[key]["nonNormalizedDuration"]),
                      str(sorterOutput[key]["iterations"]),
                      str(sorterOutput[key]["recursions"]),
                      str(sorterOutput[key]["assignments"]),
                      str(sorterOutput[key]["durationArray"]),
                      str(sorterOutput[key]["normalizedDurationArray"]),
                      str(sorterOutput[key]["sortedNums"])

                      )
      self.table.add_row(end_section=True)

  def createMetricOptions(self):
    metricOptions = dict()
    metricOptions["algorithmName"] = "Name"
    metricOptions["normalizedDuration"] = "Sorting Duration"
    if(self._metricOption == "default" or self._metricOption == "extended" or self._metricOption == "alev" or self._metricOption == "all"):
      #print("default")
      metricOptions["iterations"] = "Iterations"
      metricOptions["recursions"] = "Recursions"
      metricOptions["assignments"] = "Assignments"
      if(self._metricOption == "extended" or self._metricOption == "alev" or self._metricOption == "all"):
        #print("extended")
        metricOptions.clear()
        metricOptions["algorithmName"] = "Name"
        metricOptions["normalizedDuration"] = "Duration"
        metricOptions["nonNormalizedDuration"] = "NNORMD Duration"
        metricOptions["iterations"] = "Iterations"
        metricOptions["recursions"] = "Recursions"
        metricOptions["assignments"] = "Assignments"
        if(self._metricOption == "all" or self._metricOption == "alev"):
          #print("alev")
          metricOptions.clear()
          metricOptions["algorithmName"] = "Name"
          metricOptions["nonNormalizedDuration"] = "NNORMD Duration"
          metricOptions["normalizedDuration"] = "Duration"
          metricOptions["iterations"] = "Iterations"
          metricOptions["recursions"] = "Recursions"
          metricOptions["assignments"] = "Assignments"
          metricOptions["durationArray"] = "NNORMD Duration-Array"
          metricOptions["normalizedDurationArray"] = "Duration-Array"
          metricOptions["sortedNums"] = "Sorted Number"
          if(self._metricOption == "all"):
            #print("all")
            metricOptions.clear()
            metricOptions["algorithmName"] = "Name"
            metricOptions["nonNormalizedDuration"] = "NNORMD Duration"
            metricOptions["normalizedDuration"] = "Duration"
            metricOptions["iterations"] = "Iterations"
            metricOptions["recursions"] = "Recursions"
            metricOptions["assignments"] = "Assignments"
            metricOptions["durationArray"] = "NNORMD Duration-Array"
            metricOptions["normalizedDurationArray"] = "Duration-Array"
            metricOptions["sortedNums"] = "Sorted Number"
    return metricOptions

  def createMetaData(self, sorterOutput):
    if self._metricOption == "minimal" or self._metricOption == "default":
      return
    
    metaData = Table(show_header=True, header_style="bold blue")
    metaData.add_column("Meta Data")
    metaData.add_column("Sample Size")
    metaData.add_column("Loop Count")
    metaData.add_column("Winsorisierung")
    metaData.add_column("Number Range")
    if self._metricOption == "all":
      metaData.add_column("UN-Sorted Numbers")
      metaData.add_row("",
                        str(sorterOutput[next(iter(sorterOutput))]["elementCount"]), 
                        str(sorterOutput[next(iter(sorterOutput))]["loopCount"]),
                        str(sorterOutput[next(iter(sorterOutput))]["outliers"]),
                        str(sorterOutput[next(iter(sorterOutput))]["numberRange"]),
                        str(sorterOutput[next(iter(sorterOutput))]["origionalNums"]))
    else:
      metaData.add_row("",
                        str(sorterOutput[next(iter(sorterOutput))]["elementCount"]), 
                        str(sorterOutput[next(iter(sorterOutput))]["loopCount"]),
                        str(sorterOutput[next(iter(sorterOutput))]["outliers"]),
                        str(sorterOutput[next(iter(sorterOutput))]["numberRange"]))
    self.console.print(metaData)

  def formatMetrics(self, sorterOutput):
    os.system('clear')

    self.createMetaData(sorterOutput)
    self.createTableColumns()
    self.createTableRows(sorterOutput)


    
    self.console.print(self.table)
