# OpenSourceWorkshop - Coderage
<img src="https://github.com/shakedkialy/Coderage/blob/main/html_files/logo.png?raw=true" width="250"> 
Coderage is a package that allows running tests and code coverage in comparison over time.
The purpose of this project is to enable easy and efficient analyzing and conclusion drawing regarding software testing.  
  
  
## How to run
1. Install packages `pytest`, `pytest-cov`, `pytest-html` via `pip install`
2. Add `__ init__.py` file to the code package you want to test.
3. Name your test files `*test.py` 
 
 Example of a command line:
  `python main.py module=module1,module2 tests=test1,test2 out_dir=results`
    
If you clone our files in git use:  
`git clone https://github.com/shakedkialy/Coderage.git`  
Folders _code_ and _code2_ contain 2 code modules for example.  
Tests_Examples contains pytest test for those modules.  
The following command runs coverage on the whole directory (it ignores the package files and runs coverage on code and code2) and runs the test in the Tests_Examples folder:  
      `python main.py module=. tests=Tests_Examples`
