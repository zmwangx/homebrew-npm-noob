#!/usr/bin/env python3

import re

from noob import Package


def test_package():
    package = Package('svgo')
    formula = package.formula
    patterns = [
        re.compile(r'class Svgo < Formula'),
        re.compile(r'url "https://registry.npmjs.org/svgo/-/svgo-.*.tgz"'),
        re.compile(r'sha256 "[a-z0-9]{64}"'),
        re.compile(r'depends_on "node"'),
    ]
    for pattern in patterns:
        assert pattern.search(formula)
