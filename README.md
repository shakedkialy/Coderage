# OpenSourceWorkshop - Coderage
<img src="https://github.com/shakedkialy/Coderage/blob/main/html_files/logo.png?raw=true" width="250">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Coderage is a package that allows running tests and code coverage in comparison over time.
The purpose of this project is to enable easy and efficient analyzing and conclusion drawing regarding software testing.


## Requirements for Installing:  
- `git clone https://github.com/shakedkialy/Coderage.git`
- `pip install -e <path to package>`
- Wait for the package to be successfully installed - "Successfully installed Coderage"

## Test Your Installment:
* If you clone our files in git, the folder DemoProject contains examples files for running (module1, module2 folders contain 2 code modules for example. Tests contains pytest tests for these modules). \
enter code_examples directory ```cd DemoProject```
and run this command: \
```Coderage -m . -t Tests```
\
This command runs coverage on the whole directory and runs the tests in the Tests_Examples folder.


After this command line script is complete, you should see the following message:

      Coverage annotated source written to dir Results\annotate
      Coverage HTML written to dir Results\html
      Coverage XML written to file Results\coverage.xml

## Usage Instructions
  
1. Name your test files _test_filename_ or _filename_test_ (for pytest to recognize them as test files)

* In order to run Coderage you can use the following command: \
`Coderage -m <modules> -t <tests>`  
`Coderage -h` will display this:
  ```
  usage: Coderage [-h] [-m  [...]] [-t  [...]] [-o] [-d] [-e [[...]]]
  
  Usage: Coderage -m <Modules to test> -t <Test directory>
  
  optional arguments:
    -h, --help            show this help message and exit
    -m  [ ...], --module  [ ...]
                          Path to your tested modules
    -t  [ ...], --tests  [ ...]
                          Path to your tests directory
    -o , --out_dir        Path to your output directory
    -d , --delete_out     True/False, delete unnecessary pytest files from out
                          dir
    -e [ [ ...]], --extra_args [ [ ...]]
                          Extra args to pass pytest (call without --)
  ```

## Results
* The Coderage results located under ```Results``` folder in your project directory. Results folder created after at least one run.
  * ```Results\html``` contains HTML files where you can find graphs and analysis of your last run. 
  * ```Results\coverage```
  * ```Results\annotate```
  \
  Notice that the package automatically deletes the result files that aren't necessary for the html report.
  If you wish to keep all the files, add the parameter _delete_out=False_ to the command line. 
 
 * To view the results of this package open main_index.html (located in <Your code>/Results/html/main_index.html) via any web browser and navigate from there to all the reports.
