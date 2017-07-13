#!/usr/bin/env python3

import hashlib
import logging
import re

import jinja2
import requests

from .util import logger

DOWNLOAD_CHUNKSIZE = 65536

VERSION_SPEC_TEMPLATE = jinja2.Template('''\
url "{{ version.url }}"
version "{{ version.version }}"
sha256 "{{ version.sha256 }}"
''')

FORMULA_TEMPLATE = jinja2.Template('''\
require "language/node"

class {{ package.class_name }} < Formula
  desc "{{ package.desc }}"
  homepage "{{ package.homepage }}"
  {{ package.stable.spec|indent(2) }}

  {% if package.devel -%}
  devel do
    {{ package.devel.spec|indent(4) }}
  end

  {% endif -%}
  depends_on "node"

  def install
    system "npm", "install", *Language::Node.std_npm_install_args(libexec)
    bin.install_symlink Dir["#{libexec}/bin/*"]
  end

  test do
    raise 'Test not implemented.'
  end
end
''')


class Version(object):
    def __init__(self, version_obj):
        self.name = version_obj['name']
        self.version = version_obj['version']
        self.url = version_obj['dist']['tarball']
        sha = version_obj['dist']['shasum']
        if len(sha) == 64:
            logger.debug('Using provided sha256 checksum for %s: %s', self.url, sha)
            self.sha256 = sha
        else:
            logger.debug('Fetching %s', self.url)
            m = hashlib.sha256()
            resp = requests.get(self.url, stream=True)
            for chunk in resp.iter_content(DOWNLOAD_CHUNKSIZE):
                m.update(chunk)
            self.sha256 = m.hexdigest()

    def __str__(self):
        return '%s %s' % (self.name, self.version)

    def _repr_pretty_(self, p, cycle):
        p.text('<noob.Version "%s">' % str(self) if not cycle else '...')

    @property
    def spec(self):
        return VERSION_SPEC_TEMPLATE.render(version=self)


class Package(object):
    def __init__(self, name):
        registry_url = 'https://registry.npmjs.org/%s' % name
        logger.debug('Fetching %s', registry_url)
        resp = requests.get(registry_url)
        if resp.status_code != 200:
            raise RuntimeError('GET %s: HTTP %d' % (registry_url, resp.status_code))

        metadata = resp.json()
        self.metadata = metadata
        self.name = metadata['name']
        self.desc = metadata['description'].rstrip('.')  # strip trailing periods
        self.homepage = metadata['homepage']

        stable_ver = metadata['dist-tags']['latest']
        self.stable = Version(metadata['versions'][stable_ver])

        if 'next' in metadata['dist-tags']:
            devel_ver = metadata['dist-tags']['next']
            self.devel = Version(metadata['versions'][devel_ver])
        else:
            self.devel = None

    def __str__(self):
        desc = '%s %s' % (self.name, self.stable.version)
        if self.devel:
            desc += ', %s (devel)' % self.devel.version
        return desc

    def _repr_pretty_(self, p, cycle):
        p.text('<noob.Package "%s">' % str(self) if not cycle else '...')

    @property
    def class_name(self):
        # Convert non-alphanumeric characters to spaces, title case, then drop spaces.
        return re.sub(r'[^a-zA-Z0-9]+', ' ', self.name).title().replace(' ', '')

    @property
    def formula(self):
        return FORMULA_TEMPLATE.render(package=self)
