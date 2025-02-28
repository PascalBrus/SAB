#!/usr/bin/python3
from typing import Literal
from classes.benchmark import Benchmark
from classes.misc import colors, validateRanges
import argparse
import sys
sortingArray = ["bubble","merge","insert", "quick", "selection", "quickIter", "quickIter2"]
metricsArray = ["minimal", "default", "extended", "all"]

parser = argparse.ArgumentParser(prog="SA-Benchmark", 
                                 description="Programm takes sorting functions present in its functions directory and benchmarks those.",
                                 epilog=""
                                 )
#formatter_class=argparse.MetavarTypeHelpFormatter
#parser.add_argument("-md", "--metaData", help="Prints Header Table above Benchmark", action="store_true")
parser.add_argument("-m", "--metricsMode", help="set Metrics to display", choices=["minimal", "default", "extended", "alev", "all"], default="default")
parser.add_argument("-r", "--numberRanges", help="set the Number Array Ranges for the Benchmark", type=int, nargs="+", default=[50,-50,50])
parser.add_argument("-s", "--sortingOptions", help="set sorting Algorithms to use", choices=["bubble","merge","insert", "quick", "selection", "quickIter", "quickIter2"], nargs="+", required=True)
args = parser.parse_args()


## Literal option muste be File name of sorting Function origin
## Sorting function must have 1 and only 1 Entry point named sort()
optionArray: Literal["bubble","merge","insert", "quick", "selection", "quickIter", "quickIter2"] = []
metricsArray: Literal["minimal", "default", "extended", "all"] = "default"

ranges = {
  "count": 50,
  "lowRange": -50,
  "highRange": 50
}

rangesValid = validateRanges(args.numberRanges).validate()

if args.metricsMode == None:
  print("MetricsMode invalid!")
  print(args.metricsMode)
  sys.exit()
if not rangesValid:
  print("Range invalid!")
  print(args.numberRanges)
  sys.exit()
if args.sortingOptions == None:
   print("SortingOptions invalid!")
   print(args.sortingOptions)
   sys.exit()


#validateMetricOpt = validateArgs(sortingArray, args.sortingOptions).validate()
#validateSortingOpt = validateArgs(metricsArray, args.metricsMode).validate()

for option in args.sortingOptions:
  optionArray.append(option)


if args.metricsMode == "minimal":
  print("0")
  benchmark = Benchmark(optionArray, ranges, "minimal")
elif args.metricsMode == "default":
  print("1")
  benchmark = Benchmark(optionArray, ranges, "default")
elif args.metricsMode == "extended":
  print("2")
  benchmark = Benchmark(optionArray, ranges, "extended")
elif args.metricsMode == "alev":
  print("3")
  benchmark = Benchmark(optionArray, ranges, "alev")
elif args.metricsMode == "all":
  print("4")
  benchmark = Benchmark(optionArray, ranges, "all")


print(f"{colors.WARNING}Printed all Metrics{colors.ENDC}")
print(args)
print(optionArray)

#print(validateSortingOpt, validateMetricOpt)
