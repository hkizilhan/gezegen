#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gezegen.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gezegen.settings")
from django.core.management import execute_from_command_line

execute_from_command_line(['start.py', 'makemigrations'])
execute_from_command_line(['start.py', 'migrate'])

execute_from_command_line(['start.py', 'runserver'])

