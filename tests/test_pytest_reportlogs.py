# -*- coding: utf-8 -*-

from pytest_reportlogs import report_log


def test_steps_formatting():
    """Test short and long steps are correctly formatted"""
    a = b = 0
    assert a == b
    report_log("Simple test step description")

    a = b = 1
    assert a == b
    report_log("Very long test step description" + "* " * 100)


def test_general_log_formatting():
    """Test short and long useful information are correctly formatted"""
    a = b = 0
    assert a == b
    report_log("Simple useful information", False)

    a = b = 1
    assert a == b
    report_log("Very long useful information " + "* " * 100, False)

    a = b = 2
    assert a == b
    multiline_info = """This is a multiline information:
This is the first information.
This is another information.
"""
    report_log(multiline_info, False)


def test_mixed_steps_and_general_logs():
    """Test steps and useful information used together"""
    a = b = 0
    assert a == b
    report_log("Some test step description")
    report_log("Some useful information", False)

    a = b = 1
    assert a == b
    report_log("Some other test step description")
    report_log("Some other useful information", False)
