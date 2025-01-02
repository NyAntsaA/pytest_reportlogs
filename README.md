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
    # this info is reported as a test step
    report_log("An example of a test step", is_step=True) 

> Output:
│$ pytest test_step_example.py
|==================================== PASSES ====================================
|----------------------- Captured reported logs teardown ------------------------
|[STEP #001] An example of a test step ------------------------------------- [OK]

```

### Usage for reporting information as a normal log
```
from pytest_reportlogs import report_log

def test_simple_log_example():
    report_log("An example of useful information")

> Output:
│$ pytest test_simple_log_example.py 
|==================================== PASSES ====================================
|----------------------- Captured reported logs teardown ------------------------
|[  INFO>  ] An example of useful information 

```
