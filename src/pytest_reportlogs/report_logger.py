# -*- coding: utf-8 -*-

import logging

logging.basicConfig(level=logging.DEBUG)
REPORTLOGS_LOGGER_NAME = "pytest_reportlogs"
MAX_LOG_LENGTH = 80
STEP_PASSED_MARKER = "- [OK]"


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

    def report_log(self, msg: str, is_step: bool = False):
        """
        API for reporting useful information
        This is the only interface to be used in the tests

        Parameters
        ----------
        msg: str
            the useful information to be reported

        is_step: bool, optional
            set it to
             - True if the information should be treated as a test step
             - False if a simple useful information
            default: False

        """
        formatted_msg = self._log_formatter(msg, is_step)
        self._logs.append(formatted_msg)
        self._logger.info(formatted_msg.strip())

    def get_logs(self):
        return self._logs

    def clear_logs(self):
        self._logs = []
        self._steps_counter = 0

    def _log_formatter(self, msg, is_step=False):
        """
        Make logs pretty
            - steps logs are prefixed by `[step #]`
            - steps logs are formatted to be 80-bytes long max
        """

        formatted_msg = ""
        info_prefix = "[  INFO>  ] "
        multiline_info_prefix = " " * (len(info_prefix) + 2)

        if is_step:
            self._steps_counter += 1
            formatted_msg += f"[STEP #{self._steps_counter:03d}] {msg} "
            formatted_msg += "-" * (MAX_LOG_LENGTH - len(STEP_PASSED_MARKER))
            formatted_msg = formatted_msg[: (MAX_LOG_LENGTH - len(STEP_PASSED_MARKER))]
            formatted_msg += STEP_PASSED_MARKER + "\n"
        else:
            for j, m in enumerate(msg.splitlines()):
                # prefix = "    " if j else "> "
                prefix = multiline_info_prefix if j else info_prefix
                formatted_msg += f"{prefix}{m}\n"

        return formatted_msg
