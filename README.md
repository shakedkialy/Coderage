# OpenSourceWorkshop - Coderage
<img src="https://github.com/shakedkialy/Coderage/blob/main/html_files/logo.png?raw=true" width="250"> 

Coderage is a package that allows running tests and code coverage in comparison over time.
The purpose of this project is to enable easy and efficient analyzing and conclusion drawing regarding software testing.
    
     
## Installation:  
1. Clone repository:
`git clone https://github.com/shakedkialy/Coderage.git`

2. Install dependencies through terminal:
```
pip install pytest
pip install pytest-cov
pip install pytest-html
```

3. Test the installation passed successfully - run following command in the terminal:

```python main.py module=. tests=Tests_Examples```

## How to run:
1. Add __ init__.py file to the code package you want to test.
2. Name your test files *test.py
3. Run through command line, example: 
`python main.py module=module1,module2 tests=test1,test2 out_dir=results \
`
