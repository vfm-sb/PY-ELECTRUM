# Built-in Modules
from datetime import datetime


def get_timestamp() -> str:
    current_time = datetime.now()
    return current_time.strftime("%Y/%m")
