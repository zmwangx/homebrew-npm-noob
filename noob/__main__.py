#!/usr/bin/env python3

import argparse
import sys

from .package import Package
from .util import logger, formula_path, turn_on_debug_logging
from .version import __version__


def main():
    description = '''\
    Generate a Homebrew formula for an npm package. By default the
    generated formula is printed to stdout. If -w, --write is specified,
    the formula is directly written to the specified tap, or
    homebrew/core if no tap is specified.
    '''
    parser = argparse.ArgumentParser(prog='noob', description=description)
    add = parser.add_argument
    add('package', help='name of the package on npm')
    add('-w', '--write', action='store_true', help='write to filesystem instead of stdout')
    add('-t', '--tap', default='homebrew/core',
        help='if writing to filesystem, write to this tap instead of homebrew/core')
    add('-v', '--version', action='version', version=__version__)
    add('--debug', action='store_true')
    args = parser.parse_args()

    debug = args.debug
    if debug:
        turn_on_debug_logging()

    try:
        if args.write:
            path = formula_path(args.tap, args.package)

        package = Package(args.package)
        if args.write:
            with open(path, 'w') as fp:
                fp.write(package.formula)
            print('Formula written to %s' % path)
        else:
            sys.stdout.write(package.formula)
    except Exception as e:
        logger.error('%s: %s', type(e).__name__, e)
        if debug:
            raise


if __name__ == '__main__':
    main()
