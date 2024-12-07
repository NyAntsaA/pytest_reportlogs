class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance


class ReportLogger(Singleton):
    def __init__(self):
        self._logs = []

    def report_log(self, msg: str, is_step: bool = True):
        self._logs.append((msg, is_step))

    def get_logs(self):
        return self._logs

    def clear_logs(self):
        self._logs = []
