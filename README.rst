homebrew-npm-noob
=================

|PyPI| |License| |Build Status|

homebrew-npm-noob generates a Homebrew formula for an npm package. It is inspired by `homebrew-pypi-poet <https://github.com/tdsmith/homebrew-pypi-poet>`_.

Installation
------------

Either

::

    pip install homebrew-npm-noob

or

::

    brew install zmwangx/npm-noob/noob

Usage
-----

::

    $ noob --help
    usage: noob [-h] [-w] [-t TAP] [-v] [--debug] package

    Generate a Homebrew formula for an npm package. By default the generated
    formula is printed to stdout. If -w, --write is specified, the formula is
    directly written to the specified tap, or homebrew/core if no tap is
    specified.

    positional arguments:
      package            name of the package on npm

    optional arguments:
      -h, --help         show this help message and exit
      -w, --write        write to filesystem instead of stdout
      -t TAP, --tap TAP  if writing to filesystem, write to this tap instead of
                         homebrew/core
      -v, --version      show program's version number and exit
      --debug

License
-------

homebrew-npm-noob is released under the MIT license. See ``COPYING`` for details.

.. |PyPI| image:: https://img.shields.io/pypi/v/homebrew-npm-noob.svg?maxAge=3600
   :target: https://pypi.python.org/pypi/homebrew-npm-noob
.. |License| image:: https://img.shields.io/badge/license-MIT-blue.svg?maxAge=86400
   :target: https://github.com/zmwangx/homebrew-npm-noob/blob/master/COPYING
.. |Build Status| image:: https://travis-ci.org/zmwangx/homebrew-npm-noob.svg?branch=master
   :target: https://travis-ci.org/zmwangx/homebrew-npm-noob
