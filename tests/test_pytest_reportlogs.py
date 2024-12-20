# -*- coding: utf-8 -*-

import logging

from pytest_reportlogs import report_log

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("TestLogger")


def test_steps_formatting():
    """Test short and long steps are correctly formatted"""

    logger.info("Starting test test_steps_formatting")

    a = b = 0
    assert a == b
    report_log("Simple test step description")

    a = b = 1
    assert a == b
    report_log("Very long test step description" + "* " * 100)


def test_useful_info_formatting():
    """Test short and long useful information are correctly formatted"""

    logger.info("Starting test test_useful_info_formatting")

    a = b = 0
    assert a == b
    report_log("Simple useful information", False)

    a = b = 1
    assert a == b
    report_log("Very long useful information " + "* " * 100, False)

    a = b = 2
    assert a == b
    multiline_info = """Multiline information:
This is the first line.
This is another line.
"""
    report_log(multiline_info, False)


def test_mixed_steps_and_useful_info():
    """Test steps and useful information used together"""

    logger.info("Starting test test_mixed_steps_and_useful_info")

    a = b = 0
    assert a == b
    report_log("Some test step description")
    report_log("Some useful information", False)

    a = b = 1
    assert a == b
    report_log("Some other test step description")
    report_log("Some other useful information", False)
