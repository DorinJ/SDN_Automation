import datetime


class Entry:
    def __init__(self, address: str, available: bool, last_used: datetime.datetime):
        """
        Constructor for Entry data structure.

        self.address -> str
        self.available -> bool
        self.last_used -> datetime
        """

        self.address = address
        self.available = available
        self.last_used = last_used
