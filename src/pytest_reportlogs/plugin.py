import pytest

from pytest_reportlogs.report_logger import ReportLogger

__report_logger = ReportLogger()

report_log = __report_logger.report_log  # import this in test

MAX_LOG_LENGTH = 80
STEP_PASSED_MARKER = "- [OK]"


def _log_formatter(msg, step_nb=None):
    formatted_log = ""
    if step_nb:
        formatted_log += f"    [Step #{step_nb}] {msg} "
        formatted_log += "-" * (MAX_LOG_LENGTH - len(STEP_PASSED_MARKER))
        formatted_log = formatted_log[: (MAX_LOG_LENGTH - len(STEP_PASSED_MARKER))]
        formatted_log += STEP_PASSED_MARKER + "\n"
    else:
        for j, m in enumerate(msg.splitlines()):
            prefix = "      " if j else "    "
            formatted_log += f"{prefix}{m}\n"

    return formatted_log


@pytest.fixture(scope="function", autouse=True)
def steps_list():
    __report_logger.clear_logs()
    yield


def pytest_configure(config):
    """Report steps even for passed tests"""
    if "P" not in config.option.reportchars:
        config.option.reportchars += "P"


def pytest_runtest_teardown(item, nextitem):
    """Create a section for reported logs on teardown"""

    reported_logs = __report_logger.get_logs()

    if reported_logs:

        # format the report
        content_section = ""
        steps_counter = 0
        for data in reported_logs:
            msg, is_step = data
            if is_step:
                steps_counter += 1
                content_section += _log_formatter(msg, steps_counter)
            else:
                content_section += _log_formatter(msg)

        item.add_report_section(
            when="teardown",
            key="reported logs",
            content=content_section,
        )
