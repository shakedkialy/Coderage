# OpenSourceWorkshop - Coderage
<img src="https://github.com/shakedkialy/Coderage/blob/main/html_files/logo.png?raw=true" width="250"> 
Coderage is a package that allows running tests and code coverage in comparison over time.
The purpose of this project is to enable easy and efficient analyzing and conclusion drawing regarding software testing.


requirements for running:
    1. install the following packages:
		pytest - "python -m pip install pytest"
		pytest-cov - "python -m pip install pytest"
		pytest-html - "python -m pip install pytest"
    2. add __ init__.py file to the code package you want to test.
    3. name your test files *test.py
    4. from the command line run: 
    
		python main.py module=module1,module2 tests=test1,test2 out_dir=results
    
	We provided two code modules named 'code' and 'code2' and tests for those modules in the folder 'Tests_Examples'. To test the package, you can run from the command line the following command:
		
		python main.py module=. tests=Tests_Examples

    
     
