# -*- coding: utf-8 -*-

import logging

import pytest

from pytest_reportlogs.report_logger import (
    ReportLogger,
    REPORTLOGS_LOGGER_NAME,
)

REPORTLOGS_SECTION_HEADER = "reported logs"

__report_logger = ReportLogger()

report_log = __report_logger.report_log  # import this in test


@pytest.fixture(scope="function", autouse=True)
def steps_list():
    __report_logger.clear_logs()
    yield


def pytest_configure(config):

    # do not add logs from REPORTLOGS_LOGGER_NAME in the report
    logger = logging.getLogger(REPORTLOGS_LOGGER_NAME)
    logger.disabled = True

    # add steps/useful info even on PASSED
    if "P" not in config.option.reportchars:
        config.option.reportchars += "P"


def pytest_runtest_teardown(item, nextitem):
    """Create a section for reported logs on teardown"""

    reported_logs = __report_logger.get_logs()

    if reported_logs:
        content_section = ""
        for msg in reported_logs:
            content_section += msg

        item.add_report_section(
            when="teardown",
            key=REPORTLOGS_SECTION_HEADER,
            content=content_section,
        )
