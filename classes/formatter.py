import os
from classes.misc import colors
from rich.console import Console
from rich.table import Table
from rich import print


class Formatter:
  def __init__(self, sorterOutput):
    for element in sorterOutput:
       if isinstance(element, dict):
        for subelement, value in element.items():
          print(f"{subelement}: {value}")
    print("\n\n")
    self.printTable(sorterOutput)

  def printState(self):
    #for debugging removed
    # os.system('clear')
    # myMin= min(times)
    # myMax = max(times)
    # self.output = self.output.replace(" "+str(myMin)+"µs", (f" {colors.OKGREEN}{myMin}µs{colors.ENDC}"))
    # self.output = self.output.replace(" "+str(myMax)+"µs", (f" {colors.FAIL}{myMax}µs{colors.ENDC}"))
    # print(self.output)
    pass

  def printTable(self, sorterOutput):
    strValue = ""
    console = Console()

    table = Table(show_header=True, header_style="bold green")
    table.add_column("Metric", width=25)
    table.add_column("Value")
    for element in sorterOutput:
       if isinstance(element, dict):
        for subelement, value in element.items():
          if isinstance(value, list):
            for entry in value:
              strValue += ",  " + str(entry)
            table.add_row(subelement, strValue[3:])
            table.add_row()
            strValue = ""
          else:
            print(value)
            table.add_row(subelement, str(value))
            table.add_row()

    print("\n\n")
    console.print(table)