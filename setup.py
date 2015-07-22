#!/usr/bin/env python
from distutils.core import setup

setup(
    name = "pypushover",
    version = "0.0.1",
    url = "https://github.com/Saij/pyPushover",
    author = "Christoph Friedrich",
    scripts = ["pypushover"],
    data_files = [("/etc", ["pypushover.ini"])],
    author_email = "christoph@christophfriedrich.de",
    description = "Command-Line tool for Pushover API",
    platforms = "any",
)