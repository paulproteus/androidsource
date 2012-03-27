#!/usr/bin/env python
import os, sys, os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import vendor
vendor.vendorify()

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "android_source_site.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)


