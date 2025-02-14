import os
from classes.misc import colors
from rich.console import Console
from rich.table import Table
from rich import print

# metricsArray: Literal["minimal", "default", "extended", "all"] = ["default"]

class Formatter:
  def __init__(self, sorterOutput, metricOption):
    self._metricOption = metricOption
    # for element in sorterOutput:
    #    if isinstance(element, dict):
    #     for subelement, value in element.items():
    #       print(f"{subelement}: {value}")
    # print("\n\n")
    self.formatMetrics(sorterOutput)

  def printState(self):
    #for debugging removed
    # os.system('clear')
    # myMin= min(times)
    # myMax = max(times)
    # self.output = self.output.replace(" "+str(myMin)+"µs", (f" {colors.OKGREEN}{myMin}µs{colors.ENDC}"))
    # self.output = self.output.replace(" "+str(myMax)+"µs", (f" {colors.FAIL}{myMax}µs{colors.ENDC}"))
    # print(self.output)
    pass

  def formatMetrics(self, sorterOutput):
    os.system('clear')
    console = Console()
    metricOptions = dict()
    metricOptions["algorithmName"] = "Name"
    metricOptions["normalizedDuration"] = "Sorting Duration"
    if(self._metricOption == "default" or self._metricOption == "extended" or self._metricOption == "all"):
      #print("default")
      metricOptions["iterations"] = "Iterations"
      metricOptions["recursions"] = "Recursions"
      metricOptions["assignments"] = "Assignments"
      metricOptions["elementCount"] = "Sample Size"
      if(self._metricOption == "extended" or self._metricOption == "all"):
        #print("extended")
        metricOptions.clear()
        metricOptions["algorithmName"] = "Name"
        metricOptions["normalizedDuration"] = "Duration"
        metricOptions["nonNormalizedDuration"] = "NNORMD Duration"
        metricOptions["iterations"] = "Iterations"
        metricOptions["recursions"] = "Recursions"
        metricOptions["assignments"] = "Assignments"
        metricOptions["numberRange"] = "Number Range"
        metricOptions["elementCount"] = "Array-Length"
        metricOptions["loopCount"] = "Loop Count"
        metricOptions["outliers"] = "Outliers"
        if(self._metricOption == "all"):
          #print("all")
          metricOptions.clear()
          metricOptions["algorithmName"] = "Name"
          metricOptions["durationArray"] = "NNORMD Duration-Array"
          metricOptions["nonNormalizedDuration"] = "NNORMD Duration"
          metricOptions["normalizedDurationArray"] = "Duration-Array"
          metricOptions["normalizedDuration"] = "Duration"
          metricOptions["iterations"] = "Iterations"
          metricOptions["recursions"] = "Recursions"
          metricOptions["assignments"] = "Assignments"
          metricOptions["numberRange"] = "Number Range"
          metricOptions["elementCount"] = "Array-Length"
          metricOptions["loopCount"] = "Loop Count"
          metricOptions["outliers"] = "Outliers"
          metricOptions["origionalNums"] = "UN-Sorted Number"
          metricOptions["sortedNums"] = "Sorted Number"

    #print(metricOptions.values)
    strValue = ""
    table = Table(show_header=True, header_style="bold green")

    #adds columns to table
    for metrics in metricOptions.values():
      table.add_column(metrics)

    #adds rows to table
    for key in sorterOutput.keys():
      print(self._metricOption)
      if(self._metricOption == "minimal"):
       #print("minimal")
       table.add_row(sorterOutput[key]["algorithmName"], 
                      str(sorterOutput[key]["normalizedDuration"]))
      if(self._metricOption == "default"):
        #print("default")
        table.add_row(sorterOutput[key]["algorithmName"],
                      str(sorterOutput[key]["normalizedDuration"]),
                      str(sorterOutput[key]["iterations"]),
                      str(sorterOutput[key]["recursions"]),
                      str(sorterOutput[key]["assignments"]),
                      str(sorterOutput[key]["elementCount"]))
      if(self._metricOption == "extended"):
          #print("extended")
          table.add_row(sorterOutput[key]["algorithmName"],
                      str(sorterOutput[key]["normalizedDuration"]),
                      str(sorterOutput[key]["nonNormalizedDuration"]),
                      str(sorterOutput[key]["iterations"]),
                      str(sorterOutput[key]["recursions"]),
                      str(sorterOutput[key]["assignments"]),
                      str(sorterOutput[key]["numberRange"]),
                      str(sorterOutput[key]["elementCount"]),
                      str(sorterOutput[key]["loopCount"]),
                      str(sorterOutput[key]["outliers"]))
      if(self._metricOption == "all"):
        #print("all")
        table.add_row(sorterOutput[key]["algorithmName"],
                      str(sorterOutput[key]["durationArray"]),
                      str(sorterOutput[key]["nonNormalizedDuration"]),
                      str(sorterOutput[key]["normalizedDurationArray"]),
                      str(sorterOutput[key]["normalizedDuration"]),
                      str(sorterOutput[key]["iterations"]),
                      str(sorterOutput[key]["recursions"]),
                      str(sorterOutput[key]["assignments"]),
                      str(sorterOutput[key]["numberRange"]),
                      str(sorterOutput[key]["elementCount"]),
                      str(sorterOutput[key]["loopCount"]),
                      str(sorterOutput[key]["outliers"]),
                      str(sorterOutput[key]["origionalNums"]),
                      str(sorterOutput[key]["sortedNums"]))
      table.add_row(end_section=True)
    console.print(table)


    # {"algorithmName": self.algorithmName.capitalize(),
    #         "durationArray": self.durationArray,
    #         "nonNormalizedDuration": self.nonNormalizedDuration,
    #         "normalizedDurationArray": self.normalizedDurationArray,
    #         "normalizedDuration": self._normalizedDuration,
    #         "iterations": self.iteration,
    #         "recursions": self.recursions,
    #         "assignments": self.assignments,
    #         "numberRange": f"{self.ranges['lowRange']} : {self.ranges['highRange']}",
    #         "elementCount": self.ranges["count"],
    #         "loopCount": LOOP,
    #         "outliers": OUTLIERS,
    #         "origionalNums": self.origionalNums,
    #         "sortedNums": self.sortedNums
    #         }