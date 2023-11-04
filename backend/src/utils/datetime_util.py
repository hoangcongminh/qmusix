"""
    Contain helper function for datetime attribute
"""

from datetime import datetime

import pytz


def ict_now():
    """Current Time at ICT timezone"""
    ict_timezone = pytz.timezone("Asia/Bangkok")
    return datetime.now(ict_timezone).replace(microsecond=0)
