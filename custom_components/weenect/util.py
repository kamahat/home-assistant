"""Utility methods for weenect."""

import re
from datetime import timedelta
from typing import Optional


def parse_duration(duration: str) -> Optional[timedelta]:
    """Parse a timedelta from a weenect duration."""
    pattern = re.compile(r"\d\d[S,M,H]")

    if pattern.match(duration) is not None:
        if duration.endswith("S"):
            return timedelta(seconds=float(duration[:-1]))
        if duration.endswith("M"):
            return timedelta(minutes=float(duration[:-1]))
        if duration.endswith("H"):
            return timedelta(hours=float(duration[:-1]))
    return None
