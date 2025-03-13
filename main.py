#!/usr/bin/python3
from classes.benchmark import Benchmark
from classes.dynamicImport import DynamicImport
from classes.misc import colors, validateRanges
import argparse
import sys
from importlib import import_module

dynamicImpoter = DynamicImport()
dynamicImportedFunctions = dynamicImpoter.returnImport()

parser = argparse.ArgumentParser(prog="SA-Benchmark", 
                                 description="Programm takes sorting functions present in its functions directory and benchmarks those.",
                                 epilog=""
                                 )
parser.add_argument("-d", "--debugMode", help="Turns on some debug Information", action="store_true", default=False)
parser.add_argument("-m", "--metricsMode", help="set Metrics to display", choices=["minimal", "default", "extended", "alev", "all"], default="default")
parser.add_argument("-r", "--numberRanges", help="set the Number Array Ranges for the Benchmark", type=int, nargs="+", default=[50,-50,50])
mutualGroup = parser.add_mutually_exclusive_group()
mutualGroup.add_argument("-i", "--includeSortAlgo", help="set sorting Algorithms to use", choices=dynamicImportedFunctions.keys(), nargs="+")
mutualGroup.add_argument("-e", "--excludeSortAlgo", help="exclude sorting Algorithms to use", choices=dynamicImportedFunctions.keys(), nargs="+")

args = parser.parse_args()


ranges = {
  "count": 250,
  "lowRange": -50,
  "highRange": 50
}

rangesValid = validateRanges(args.numberRanges).validate()
if args.includeSortAlgo == None and args.excludeSortAlgo == None:
  functionRefs = dynamicImportedFunctions
if args.includeSortAlgo != None:
  functionRefs= dynamicImpoter.includeFunctionRefs(dynamicImportedFunctions, args.includeSortAlgo)
if args.excludeSortAlgo != None:
  functionRefs= dynamicImpoter.excludeFunctionRefs(dynamicImportedFunctions, args.excludeSortAlgo)



if not rangesValid:
  print("Range invalid!")
  print(args.numberRanges)
  sys.exit()

benchmark = Benchmark(functionRefs, args.numberRanges, args.metricsMode)


print(f"{colors.WARNING}Printed all Metrics{colors.ENDC}")
if (args.debugMode):
  print(args)
  print(args.sortingOptions)

#print(validateSortingOpt, validateMetricOpt)
