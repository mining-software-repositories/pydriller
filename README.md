# SysRepo Analyze
A set of python scripts to create analysis reports of software repositories.

This repository has a lot of python's scripts using the pydriller (https://github.com/ishepard/pydriller) to analyze and mining data from software repositories. 

The software repository analysed is https://github.com/armandossrecife/promocity

How to generate the reports?
---

1. Install pydriller via pip
```
$ pip install pydriller
```
2. Run the script python
```
$ python general_information.py > report-repository.txt
```
3. Run the script python
```
$ python main.py
```
4. The following files are automatically generated after the analysis is finished. 
```
$ img/repository_name.png
$ json/repository_name.json
```
5. Performing tests
```
pip install pytest pytest-html
pytest -v test_utilities.py --html=pytest_report_test_utilities.html --self-contained-html
pytest -v test_check_commits.py --html=pytest_report_test_check_commits.html --self-contained-html
```
