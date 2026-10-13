"""Input parsing and validation helpers."""

import re
from datetime import datetime

from ..constants import MAX_AGE_MONTHS, APPROVED_STATUSES


def parse_date(text):
    """Return a real YYYY-MM-DD date, or None when input is invalid."""
    text = text.strip()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", text):
        return None
    try:
        return datetime.strptime(text, "%Y-%m-%d").date()
    except ValueError:
        return None


def parse_age(text):
    """Return age in months from 0 to MAX_AGE_MONTHS, or None when invalid."""
    text = text.strip()
    if text.isascii() and text.isdigit() and len(text) <= 4:
        age = int(text)
        if age <= MAX_AGE_MONTHS:
            return age
    return None


def normalise_status(text):
    """Normalise a numeric option or case-insensitive status name."""
    text = text.strip()
    if text in ("1", "2", "3"):
        return APPROVED_STATUSES[int(text) - 1]
    for status in APPROVED_STATUSES:
        if text.lower() == status.lower():
            return status
    return text
