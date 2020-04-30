#!/usr/bin/env python3

"""Jinja lint

This script lints (validates) Jinja files.

Copyright (C) 2020 Peter Mosmans [Go Forward]
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""


import sys
from jinja2 import Environment, exceptions


def validate(filename):
    """Validate Jinja template."""
    env = Environment()
    try:
        with open(filename) as template:
            print("Validating {0}".format(filename))
            _rendered = env.parse(template.read())
    except FileNotFoundError as exception:
        print("Could not open file {0}: {1}".format(filename, exception),
              file=sys.stderr)
    except exceptions.TemplateSyntaxError as exception:
        print("Syntax error in {0}: {1}".format(filename, exception),
              file=sys.stderr)
        sys.exit(-1)


def main():
    """Main program loop."""
    for filename in sys.argv[1:]:
        validate(filename)


if __name__ == "__main__":
    main()
