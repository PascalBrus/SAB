# SAB - Sorting Algorithm Benchmark

## Usage:

```
sab [ -m <metricsMode> { minimal, default, extended, alev, all } ]
    [ -r <numberRanges> { int, int, int } ]
      -s <sortingOptions> { bubble, merge, insert, quick, selection, quickIter, quickIter2, sort, args... }
```

| option                             | value                                                                                       | type   |
| ---------------------------------- | ------------------------------------------------------------------------------------------- | ------ |
| [metricsMode](#MetricsMode)        | [minimal](#minimal); [default](#default); [extended](#extended); [alev](#alev); [all](#all) | String |
| [numberRanges](#Number-Ranges)     | Int, Int, Int                                                                               | Int    |
| [sortingOptions](#Sorting-Options) | bubble, merge, insert, quick, selection, quickIter, quickIter2, args...                     | String |

**by Default sortingOptions will have the upper functions available see [Adding your own Sorting Algorithms](#Adding-your-own-Sortig-Algorithm) to add more wich are gonna be accessable like above**

### MetricsMode

Metrics Mode is an optional parameter when using sab. The default setting of it is set to `metricsMode: default`.

#### Every option is gonna build opon the last one. So default will have every Metric minimal does plus the ones listed below.

##### minimal

- [Name](#Name)
- [Sorting Duration](#Sorting-Duration)

##### default

- [Iterations](#Iterations)
- [Recursions](#Recursions)
- [Assignments](#Assignments)

##### extended

###### From Extended onwards you are gonna get a new Table with "Meta Data"

- Meta Data:
  - [Sample Size](#Sample-Size)
  - [Loop Count](#Loop-Count)
  - [Winsorization](#Winsorization)
  - [Number Range](#Number Range)

##### alev

(**AL**most-**EV**erything)

- [NNORMD Dutation](#NNORMD-Dutation) (Non Normalized Duration)
- [NNORMD Duration-Array](#NNORMD-Duration-Array) (Non Normalized Duration Array)
- [Duration-Array](#Duration-Array)

##### all

- Meta Data:
  - [UN-Sorted Numbers](#UN-Sorted-Numbers)
- [Sorted Numbers](#Sorted-Numbers)

### Number Ranges

The Number Ranges is an optional parameter when using sab and sets the [Sample Size](#Sample-Size) and lower and higher threasholds of [Number Range](#Number-Range). The default of it is set to `Sample Size: 50` / `lower number treashold: -50` / `upper number threashold: 50`

#### The parameter Number Ranges is gonna take 3 Integer.

1. The first Number is gonna set the [Sample Size](#Sample-Size) of the benchmark test
2. The second Number is gonna set the lower threashold of the [Number Range](#Number-Range)
3. The third Number is gonna set the upper threashold of the [Number Range](#Number-Range)

### Sorting Options

> Sorting Options is a **mandatory** parameter when using sab. It has no default Value.

There are 2 Ways to determin wich algorithms to run.

1. Include [-i ; --include]
2. Exclude [-e ; --exclude]

Include: With the include option you say wich Algorithm you want to **include** for your Benchmark

Exclude: With the exclude option you say wich Algorith you wanna **exclude** from your Benchmark. Therefore it will run **all** avialable Algorithm excluding the ones you set.

> Include | Exclude are mutually exclusive. Means you can only choose one mode. If no option is present the Benchmark will include all Algorithms.

Default Sorting Algorithms avialable are:

- bubble
- merge
- insert
- quick
- selection
- quickIter
- quickIter2

For an extensive list of allowed values use `sab.py -h`. Allowed values are gonna depend on your /functions directory as they are dynamically read from there and added as possible values. <br>See [Adding your own Sorting Algorithms](#Adding-your-own-Sortig-Algorithm) for a Guide on how to add your own/custom sorting Algorithms.

## Metrics

Metrics is the data gathered during the sorting process. Its gonna be presented in a green Table after successfully running the programm.

#### Meta Data

Meta Data is the Data wich is displayed from the [metricsMode](#MetricsMode) option [extended](#extended) and onwards. Its gonna be printed ABOVE the green metrics table as a blue table and will contain meta data applying to every sorting algorithm tested.

## Metrics explained

#### Name:

Name of the Sorting Algorithms used. Name is dynamically read from filename

#### Sorting Duration:

The Average Duration it took for that Search Algorithm to complete its cycle. The Benchmark uses 20 [Loops](#Loop-Count) and 4 data points for [Winsorization](#Winsorization) and then calculates a normalized average.

#### Iterations:

The number of times you repeat a Loop. Entering a Loop and immediately leaving it counts as 1 Iteration. The Metric for Iterations therefore counts up every time at the start of a loop as a first Instruction.<br>See [Adding your own Sorting Algorithms](##Adding-your-own-Sortig-Algorithm) to correctly implement the Iteration metric into your own search algorithm.

### Recursions:

The number of times the main search Function gets called. Functions that sort Iterative and not recursive count as 1 Recursion. The Metric for Recursion therefore counts up every time at the start of the Function as a first Instruction.<br>See [Adding your own Sorting Algorithms](##Adding-your-own-Sortig-Algorithm) to correctly implement the Recursion metric into your own search algorithm.

### Assignments:

The number of times the search Algorithm assigns a Number to his output/helper Arrays/etc. .The Metric for Assignments therefore counts up everytime you assign a Number to an output/helper Arrays/etc. to store/swap it.<br>See [Adding your own Sorting Algorithms](##Adding-your-own-Sortig-Algorithm) to correctly implement the Recursion metric into your own search algorithm.

### Sample Size:

Sample size reflects how large the Sorted Array of Numbers is.<br>See [Usage](#) to see how to set your desired Sample Size.

### Loop Count:

Loop Count reflects how often the Search Algorithm is being tested. So a Loop Count of 10 means it sorted the Numbers 10 times.

### Winsorization:

Winsorization is the count of data points wich are discarded as extreme outliers in an attempt to somewhat normalize the Sorting Times and create an average. So a Winsorization of 4 would mean the 2 lowest and highest sorting times are discarded.

### Number Range:

Number Range is the Range of Numbers the random Array chooses a random Number from. So a range of -50 to 50 would mean the only possible numbers in the number array is -50 to 50

### NNORMD Dutation:

The Non Normalized Duration is the average sorting time the Algorithm took to sort the Numbers BEFORE [Winsorizing](#Winsorization) any times.

### NNORMD Duration-Array:

The Non Normalized Duration Array are all of the times the Algorithm sorted the Numbers BEFORE [Winsorizing](#Winsorization) any of them.

### Duration-Array:

The Duration Array are all of the times the Algorithm sorted the Numbers AFTER [Winsorizing](#Winsorization) them. These are the times used to create [Sorting Duration](#Sorting-Duration)

### UN-Sorted Numbers:

The un-sorted Numbers is the origional Number Array before sorting it.<br>Its hidden in every [Metrics Option](#MetricsMode) other than [all](#all) because of the usually very high [Sample Size](#Sample-Size)

### Sorted Numbers:

The Sorted Numbers are the Numbers after being sorted by the Algorithm.<br>Its hidden in every [Metrics Option](#MetricsMode) other than [all](#all) because of the usually very high [Sample Size](#Sample-Size)

## Adding your own Sortig Algorithm:

If you wanna add your own sorting Algorithm you only need to add a new python file into the functions directory. The Name of the Algorithm is the name of the file you add. The File should have following syntax:

```
def sort(info numbers):
  def your_sort_algorithm(info, nums):
    #Stuff
    return sorted_numbers

return your_sort_algorithm(info, nums)
```

Your sorting algorithm is then gonna be listed under the help syntax as choice when trying to use SAB or with `"python3 main.py -h"`

# UNDER CONSTRUCTION
