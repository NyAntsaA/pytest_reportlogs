# pytest_reportlogs

pytest_reportlogs is a plugin for [pytest](https://docs.pytest.org/en/stable/) allowing to add useful information *(logs)* into the test report.

It was initially meant for adding test steps into the report, but then was extended to add any kind of *useful* information.

It reports the logged information even when the outcome is *PASSED*.


## Installation

It is recommended to install this plugin in a self-contained environment.

```
pip install git+https://github.com/NyAntsaA/pytest_reportlogs
```


## Usage

Import and use **report_log** in the test file.

### Usage for reporting information as a test step
```
from pytest_reportlogs import report_log

def test_step_example():
    report_log("An example of a test step")  # this info is reported as a test step

> Output:
│$ pytest test_step_example.py
│===================================== test session starts ======================================
│test_step_example.py .                                                                   [100%]
│
│============================================ PASSES ============================================
│------------------------------- Captured reported logs teardown --------------------------------
│    [Step #1] An example of a test step ------------------------------------ [OK]
│====================================== 1 passed in 0.01s =======================================


```

### Usage for reporting information as a normal log
```
from pytest_reportlogs import report_log

def test_log_example():
    # report info without formatting it as a test step -> 2nd arg False
    report_log("An example of useful information", False)

> Output:
│$ pytest test_log_example.py 
│===================================== test session starts ======================================
│test_log_example.py .                                                                    [100%]
│
│============================================ PASSES ============================================
│------------------------------- Captured reported logs teardown --------------------------------
│        An example of useful information
│====================================== 1 passed in 0.01s =======================================

```
