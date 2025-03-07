import os
from queue import Full
from classes.misc import colors
from rich.console import Console
from rich.table import Table
from rich import print
from classes.misc import colors

# metricsArray: Literal["minimal", "default", "extended", "all"] = ["default"]

class Formatter:
  def __init__(self, sorterOutput, metricOption):
    self._metricOption = metricOption
    self.mode = " µs"
    self.adjustTimes(sorterOutput)
    self.formatSortingMetricNumbers(sorterOutput)
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

  def formatSortingMetricNumbers(self, sorterOutput):
    for key in sorterOutput.keys():
      sorterOutput[key]["iterations"] = "{:,}".format(sorterOutput[key]["iterations"]).replace("," ,".")
      sorterOutput[key]["recursions"] = "{:,}".format(sorterOutput[key]["recursions"]).replace("," ,".")
      sorterOutput[key]["assignments"] = "{:,}".format(sorterOutput[key]["assignments"]).replace("," ,".")



  def colorTimes(self, sorterOutput):
    min = float("inf");
    minKey = ""
    max = float("-inf")
    maxKey = ""
    for key in sorterOutput.keys():
      if sorterOutput[key]["normalizedDuration"] > max:
        max = sorterOutput[key]["normalizedDuration"]
        maxKey = key
      if sorterOutput[key]["normalizedDuration"] < min:
        min = sorterOutput[key]["normalizedDuration"]
        minKey = key

    if min == max and minKey == maxKey:
      min = float("inf")
      minKey = ""
    else:
      sorterOutput[minKey]["normalizedDuration"] = f"[bold green]{sorterOutput[minKey]['normalizedDuration']}[/bold green]"
    sorterOutput[maxKey]["normalizedDuration"] = f"[bold red]{sorterOutput[maxKey]['normalizedDuration']}[/bold red]"

    return sorterOutput

  def setMode(self, sorterOutput):
    for key in sorterOutput.keys():
      if float(sorterOutput[key]["normalizedDuration"]) / 1000 / 1000 > 1:
        print("its s")
        self.mode = " s"
        return 
      if float(sorterOutput[key]["normalizedDuration"]) >= 1000:
        print("its ms")
        self.mode = " ms"
        continue 

  def adjustTimes(self, sorterOutput):
    #checks how long it took and converts it from µs to either µs, ms or s
    self.setMode(sorterOutput)
    for key in sorterOutput.keys():
      if self.mode == " ms":
        sorterOutput[key]["normalizedDuration"] = float(sorterOutput[key]["normalizedDuration"]) / 1000
      elif self.mode == " s":
        sorterOutput[key]["normalizedDuration"] = float(sorterOutput[key]["normalizedDuration"]) / 1000 / 1000

  def createTableRows(self, sorterOutput):
    
    sorterOutput = self.colorTimes(sorterOutput)

    for key in sorterOutput.keys():
      #print(self._metricOption)
      if(self._metricOption == "minimal"):
       #print("minimal")
       self.table.add_row(sorterOutput[key]["algorithmName"], 
                      str(sorterOutput[key]["normalizedDuration"])+self.mode)
      if(self._metricOption == "default"):
        #print("default")
        self.table.add_row(sorterOutput[key]["algorithmName"],
                      str(sorterOutput[key]["normalizedDuration"])+self.mode,
                      str(sorterOutput[key]["iterations"]),
                      str(sorterOutput[key]["recursions"]),
                      str(sorterOutput[key]["assignments"]))
      if(self._metricOption == "extended"):
          #print("extended")
          self.table.add_row(sorterOutput[key]["algorithmName"],
                      str(sorterOutput[key]["normalizedDuration"])+self.mode,
                      str(sorterOutput[key]["nonNormalizedDuration"])+" ms",
                      str(sorterOutput[key]["iterations"]),
                      str(sorterOutput[key]["recursions"]),
                      str(sorterOutput[key]["assignments"]))
      if(self._metricOption == "alev"):
        #print("alev")
        self.table.add_row(sorterOutput[key]["algorithmName"],
                      str(sorterOutput[key]["normalizedDuration"])+self.mode,
                      str(sorterOutput[key]["nonNormalizedDuration"])+" ms",
                      str(sorterOutput[key]["iterations"]),
                      str(sorterOutput[key]["recursions"]),
                      str(sorterOutput[key]["assignments"]),
                      str(sorterOutput[key]["durationArray"])[1:-1],
                      str(sorterOutput[key]["normalizedDurationArray"])[1:-1])
      if(self._metricOption == "all"):
        #print("all")
        self.table.add_row(sorterOutput[key]["algorithmName"],
                      str(sorterOutput[key]["normalizedDuration"])+self.mode,
                      str(sorterOutput[key]["nonNormalizedDuration"])+" ms",
                      str(sorterOutput[key]["iterations"]),
                      str(sorterOutput[key]["recursions"]),
                      str(sorterOutput[key]["assignments"]),
                      str(sorterOutput[key]["durationArray"])[1:-1],
                      str(sorterOutput[key]["normalizedDurationArray"])[1:-1],
                      str(sorterOutput[key]["sortedNums"])[1:-1])
      self.table.add_row(end_section=True)

  def createMetricOptions(self):
    metricOptions = dict()
    metricOptions["algorithmName"] = "Name"
    metricOptions["normalizedDuration"] = f"Sorting Duration in{self.mode}"
    if(self._metricOption == "default" or self._metricOption == "extended" or self._metricOption == "alev" or self._metricOption == "all"):
      #print("default")
      metricOptions["iterations"] = "Iterations"
      metricOptions["recursions"] = "Recursions"
      metricOptions["assignments"] = "Assignments"
      if(self._metricOption == "extended" or self._metricOption == "alev" or self._metricOption == "all"):
        #print("extended")
        metricOptions.clear()
        metricOptions["algorithmName"] = "Name"
        metricOptions["normalizedDuration"] = f"Duration in{self.mode}"
        metricOptions["nonNormalizedDuration"] = "NNORMD Duration in ms"
        metricOptions["iterations"] = "Iterations"
        metricOptions["recursions"] = "Recursions"
        metricOptions["assignments"] = "Assignments"
        if(self._metricOption == "all" or self._metricOption == "alev"):
          #print("alev")
          metricOptions.clear()
          metricOptions["algorithmName"] = "Name"
          metricOptions["nonNormalizedDuration"] = "NNORMD Duration in ms"
          metricOptions["normalizedDuration"] = f"Duration in{self.mode}"
          metricOptions["iterations"] = "Iterations"
          metricOptions["recursions"] = "Recursions"
          metricOptions["assignments"] = "Assignments"
          metricOptions["durationArray"] = "NNORMD Duration-Array"
          metricOptions["normalizedDurationArray"] = "Duration-Array"
          if(self._metricOption == "all"):
            #print("all")
            metricOptions.clear()
            metricOptions["algorithmName"] = "Name"
            metricOptions["nonNormalizedDuration"] = "NNORMD Duration in ms"
            metricOptions["normalizedDuration"] = f"Duration in{self.mode}"
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
                        str(sorterOutput[next(iter(sorterOutput))]["origionalNums"])[1:-1])
    else:
      metaData.add_row("",
                        str(sorterOutput[next(iter(sorterOutput))]["elementCount"]), 
                        str(sorterOutput[next(iter(sorterOutput))]["loopCount"]),
                        str(sorterOutput[next(iter(sorterOutput))]["outliers"]),
                        str(sorterOutput[next(iter(sorterOutput))]["numberRange"]))
    self.console.print(metaData)

  def formatMetrics(self, sorterOutput):
    #os.system('clear')

    self.createMetaData(sorterOutput)
    self.createTableColumns()
    self.createTableRows(sorterOutput)
    
    self.console.print(self.table)
