#!/usr/bin/env python
import os
import site
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line
    # site.addsitedir('testapp')
    execute_from_command_line(sys.argv)
