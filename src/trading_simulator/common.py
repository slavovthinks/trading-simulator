"""
A module for common functions
"""

import datetime

def to_date_string(d: datetime.datetime):
    """
    Parses a datetime.datetime object to YYYY-MM-DD formatted string
    """
    return d.strftime('%Y-%m-%d')
