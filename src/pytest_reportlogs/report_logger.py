# -*- coding: utf-8 -*-

import logging

logging.basicConfig(level=logging.DEBUG)
REPORTLOGS_LOGGER_NAME = "pytest_reportlogs"
MAX_LOG_LENGTH = 80
STEP_PASSED_MARKER = "- [PASS]"
STEP_FAILED_MARKER = "- [FAIL]"


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance


class ReportLogger(Singleton):
    def __init__(self):
        self._logs = []
        self._steps_counter = 0
        self._logger = logging.getLogger(REPORTLOGS_LOGGER_NAME)

    def report_log(self, msg: str, step_status: bool = None):
        """
        API for reporting useful information
        This is the only interface to be used in the tests

        Parameters
        ----------
        msg: str
            the useful information to be reported

        step_status: bool, optional
            If not set, the information is treated as a normal log

            Set it to
             - True if the information should be treated as a PASSED step
             - False if the information should be treated as a FAILED step
            default: None

        """
        formatted_msg = self._log_formatter(msg, step_status)
        self._logs.append(formatted_msg)
        if step_status is False:
            self._logger.error(formatted_msg.strip())
        else:
            self._logger.info(formatted_msg.strip())

    def get_logs(self):
        return self._logs

    def clear_logs(self):
        self._logs = []
        self._steps_counter = 0

    def _log_formatter(self, msg, step_status=False):
        """
        Make logs pretty
            - steps logs are prefixed by `[step #]`
            - steps logs are formatted to be 80-bytes long max
        """

        formatted_msg = ""
        info_prefix = "[  INFO>  ] "
        multiline_info_prefix = " " * (len(info_prefix) + 2)

        if step_status is not None:
            self._steps_counter += 1
            formatted_msg += f"[STEP #{self._steps_counter:03d}] {msg} "
            marker = STEP_PASSED_MARKER if step_status else STEP_FAILED_MARKER
            formatted_msg += "-" * (MAX_LOG_LENGTH - len(marker))
            formatted_msg = formatted_msg[: (MAX_LOG_LENGTH - len(marker))]
            formatted_msg += marker + "\n"
        else:
            for j, m in enumerate(msg.splitlines()):
                prefix = multiline_info_prefix if j else info_prefix
                formatted_msg += f"{prefix}{m}\n"

        return formatted_msg
