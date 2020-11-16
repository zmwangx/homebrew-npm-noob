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
      url "https://registry.npmjs.org/babel-cli/-/babel-cli-6.26.0.tgz"
      sha256 "81ac501721ff18200581c58542fa6226986766c53be35ad8f921fabd47834d02"
      license "MIT"

      livecheck do
        url :stable
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
.. |Build Status| image:: https://github.com/zmwangx/homebrew-npm-noob/workflows/test/badge.svg
   :target: https://github.com/zmwangx/homebrew-npm-noob/actions
