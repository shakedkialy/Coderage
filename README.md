# OpenSourceWorkshop - Coderage
<img src="https://github.com/shakedkialy/Coderage/blob/main/html_files/logo.png?raw=true" width="250"> 
Coderage is a package that allows running tests and code coverage in comparison over time.
The purpose of this project is to enable easy and efficient analyzing and conclusion drawing regarding software testing.


# Run Example:
![image](https://user-images.githubusercontent.com/44695990/121694086-6fa59e80-cad2-11eb-80f7-0905da6f68c9.png)

# Installation instructions:
- install python on your PC with pip
- run pip install pytest pytest-cov pytest-html

# Running instructions: \
    1. Make sure you have the requirements packages before running the program
    2. add __ init__.py file to the code package you want to test. \
    3. name your test files *test.py \
    4. command line for example: \
    
      python main.py module=module1,module2 tests=test1,test2 out_dir=results \
    
    if you clone our files in git, code and code2 folders contain 2 code modules for example. Tests_Examples contains pytest test for those modules.
    This command runs coverage on the whole directory (ignores the package files and runs coverage on code and code2) and runs the test in the Tests_Examples folder. 
    
      python main.py module=. tests=Tests_Examples
    
     
