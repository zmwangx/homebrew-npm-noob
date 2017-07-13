#!/usr/bin/env python3

import logging
import os
import subprocess

logging.basicConfig(format='[%(levelname)s] %(message)s')
logger = logging.getLogger('noob')


def formula_path(tap, formula):
    try:
        tap_root = subprocess.check_output(['brew', '--repo', tap]).decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        raise RuntimeError('`brew --repo %s` failed with code %d: %s' %
                           (tap, e.returncode, e.output))
    if not os.path.exists(tap_root):
        raise RuntimeError('Tap path %s does not exist' % tap_root)

    for subdir in ['Formula', 'HomebrewFormula']:
        formulae_dir = os.path.join(tap_root, subdir)
        if os.path.exists(formulae_dir):
            break
    else:
        formulae_dir = tap_root

    return os.path.join(formulae_dir, '%s.rb' % formula)


def turn_on_debug_logging():
    logger.setLevel(logging.DEBUG)
