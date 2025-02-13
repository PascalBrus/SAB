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
    self.printMetrics(sorterOutput)

  def printState(self):
    #for debugging removed
    # os.system('clear')
    # myMin= min(times)
    # myMax = max(times)
    # self.output = self.output.replace(" "+str(myMin)+"µs", (f" {colors.OKGREEN}{myMin}µs{colors.ENDC}"))
    # self.output = self.output.replace(" "+str(myMax)+"µs", (f" {colors.FAIL}{myMax}µs{colors.ENDC}"))
    # print(self.output)
    pass

  def printMetrics(self, sorterOutput):
    metricOptions = dict()
    
    metricOptions["algorithmName"] = "Name"
    metricOptions["normalizedDuration"] = "Sorting Duration"
    if(self._metricOption == "default" or self._metricOption == "extended" or self._metricOption == "all"):
      #print("default")
      metricOptions["iterations"] = "Iterations"
      metricOptions["recursions"] = "Recursions"
      metricOptions["assignments"] = "Assignments"
      if(self._metricOption == "extended" or self._metricOption == "all"):
        #print("extended")
        metricOptions["elementCount"] = "Array-Length"
        metricOptions["lowNumsTreshold"] = "lowest Number"
        metricOptions["highNumsTreshold"] = "highest Number"
        metricOptions["origionalNums"] = "UN-Sorted Number"
        metricOptions["sortedNums"] = "Sorted Number"
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
          metricOptions["lowNumsTreshold"] = "lowest Number"
          metricOptions["highNumsTreshold"] = "highest Number"
          metricOptions["elementCount"] = "Array-Length"
          metricOptions["loopCount"] = "Loop Count"
          metricOptions["outliers"] = "Outliers"
          metricOptions["origionalNums"] = "UN-Sorted Number"
          metricOptions["sortedNums"] = "Sorted Number"

    #print(metricOptions.values)
    strValue = ""
    console = Console()

    table = Table(show_header=True, header_style="bold green")
    for metrics in metricOptions.values():
      table.add_column(metrics)
    #for metricValue in sorterOutput:
    if(self._metricOption == "minimal"):
    #print("minimal")
      table.add_row(sorterOutput["algorithmName"], 
                    sorterOutput["normalizedDuration"])
    if(self._metricOption == "default"):
      #print("default")
      table.add_row(sorterOutput["algorithmName"],
                    sorterOutput["normalizedDuration"],
                    sorterOutput["iterations"],
                    sorterOutput["recursions"],
                    sorterOutput["assignments"]
                    )
    if(self._metricOption == "extended"):
        #print("extended")
        table.add_row(sorterOutput["algorithmName"],
                    sorterOutput["normalizedDuration"],
                    sorterOutput["iterations"],
                    sorterOutput["recursions"],
                    sorterOutput["assignments"],
                    sorterOutput["elementCount"],
                    sorterOutput["lowNumsTreshold"],
                    sorterOutput["highNumsTreshold"],
                    sorterOutput["origionalNums"],
                    sorterOutput["sortedNums"]

                    )
    if(self._metricOption == "all"):
      #print("all")
      table.add_row(sorterOutput["algorithmName"],
                    sorterOutput["durationArray"],
                    sorterOutput["nonNormalizedDuration"],
                    sorterOutput["normalizedDurationArray"],
                    sorterOutput["normalizedDuration"],
                    sorterOutput["iterations"],
                    sorterOutput["recursions"],
                    sorterOutput["assignments"],
                    sorterOutput["lowNumsTreshold"],
                    sorterOutput["highNumsTreshold"],
                    sorterOutput["elementCount"],
                    sorterOutput["loopCount"],
                    sorterOutput["outliers"],
                    sorterOutput["origionalNums"],
                    sorterOutput["sortedNums"],
                    )
    #print(sorterOutput)
    # for element in sorterOutput:
    #    if isinstance(element, dict):
    #     for subelement, value in element.items():
    #       if isinstance(value, list):
    #         for entry in value:
    #           strValue += ",  " + str(entry)
    #         table.add_column(subelement, strValue[3:])
    #         strValue = ""
    #       else:
    #         print(value)
    #         table.add_column(subelement, str(value))

    #print("\n\n")
    console.print(table)