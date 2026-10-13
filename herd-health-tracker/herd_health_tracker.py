"""Compatibility launcher for Herd Health Tracker.

The implementation is organized in the herd_health_tracker_app package.
This root-level launcher keeps the simple command `python herd_health_tracker.py`
working and re-exports the public functions used by the test suite.
"""

from herd_health_tracker_app import *  # noqa: F401,F403 - public compatibility facade
from herd_health_tracker_app import __all__ as __all__

if __name__ == "__main__":
    main()
