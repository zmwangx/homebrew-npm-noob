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

Example
-------

.. code:: ruby

    $ noob babel-cli
    require "language/node"

    class BabelCli < Formula
      desc "Babel command line"
      homepage "https://babeljs.io/"
      url "https://registry.npmjs.org/babel-cli/-/babel-cli-6.24.1.tgz"
      version "6.24.1"
      sha256 "d69a00bdb4f35184cda1f5bfe8075cd4d569600b8e61d864d1f08e360367933b"

      devel do
        url "https://registry.npmjs.org/babel-cli/-/babel-cli-7.0.0-alpha.15.tgz"
        version "7.0.0-alpha.15"
        sha256 "e825b9fe8e578aa392a8b398950070d3816c4c75e99953adb07ccfe858aea454"
      end

      depends_on "node"

      def install
        system "npm", "install", *Language::Node.std_npm_install_args(libexec)
        bin.install_symlink Dir["#{libexec}/bin/*"]
      end

      test do
        raise "Test not implemented."
      end
    end

See Also
--------

`Node for Formula Authors <https://github.com/Homebrew/brew/blob/master/docs/Node-for-Formula-Authors.md>`_ in Homebrew's docs.

License
-------

homebrew-npm-noob is released under the MIT license. See ``COPYING`` for details.

.. |PyPI| image:: https://img.shields.io/pypi/v/homebrew-npm-noob.svg?maxAge=3600
   :target: https://pypi.python.org/pypi/homebrew-npm-noob
.. |License| image:: https://img.shields.io/badge/license-MIT-blue.svg?maxAge=86400
   :target: https://github.com/zmwangx/homebrew-npm-noob/blob/master/COPYING
.. |Build Status| image:: https://travis-ci.org/zmwangx/homebrew-npm-noob.svg?branch=master
   :target: https://travis-ci.org/zmwangx/homebrew-npm-noob
