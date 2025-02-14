#!/usr/bin/python3
from typing import Literal
from classes.benchmark import Benchmark
from classes.misc import colors

## Literal option muste be File name of sorting Function origin
## Sorting function must have 1 and only 1 Entry point named sort()
optionArray: Literal["bubble","merge","insert", "quick", "selection", "quickIter", "quickIter2"] = ["bubble", "merge"]
metricsArray: Literal["minimal", "default", "extended", "all"] = "default"

ranges = {
  "count": 10,
  "lowRange": -50,
  "highRange": 50
}
#benchmark = Benchmark(optionArray, ranges, "minimal")
#benchmark = Benchmark(optionArray, ranges, "default")
#benchmark = Benchmark(optionArray, ranges, "extended")
benchmark = Benchmark(optionArray, ranges, "all")


print(f"{colors.WARNING}Printed all avialable Steps{colors.ENDC}")