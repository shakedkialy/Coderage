# OpenSourceWorkshop - Coderage
<img src="https://github.com/shakedkialy/Coderage/blob/main/html_files/logo.png?raw=true" width="250"> 
Coderage is a package that allows running tests and code coverage in comparison over time.
The purpose of this project is to enable easy and efficient analyzing and conclusion drawing regarding software testing.


requirements for running: \
    packages: pytest, pytest-cov, pytest-html (via pip install) \
        1. Add __ init__.py file to the code package you want to test. \
        2. Name your test files *test.py \
        3. Command line structure: 
  
    python main.py module=module1,module2 tests=test1,test2 out_dir=results

The project contains code and code2 example modules for example.
Test_Examples contains pytest tests for the example modules, running the following command will run the tests on the examples modules.       
  
    python main.py module=. tests=Tests_Examples

       
     
