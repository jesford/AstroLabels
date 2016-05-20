try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

DESCRIPTION = "AstroLabels"
LONG_DESCRIPTION = """
AstroLabels
======================================================
A set of common (for me) strings used to label astronomy plots. Add your own!
"""
NAME = "AstroLabels"
AUTHOR = "Jes Ford"
AUTHOR_EMAIL = "jesford@uw.edu"
MAINTAINER = "Jes Ford"
MAINTAINER_EMAIL = "jesford@uw.edu"
URL = 'http://github.com/jesford/AstroLabels'
DOWNLOAD_URL = 'http://github.com/jesford/AstroLabels'
LICENSE = 'MIT'
VERSION = '0.1'

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      url=URL,
      download_url=DOWNLOAD_URL,
      license=LICENSE,
      packages=['astrolabels', 'astrolabels/tests'],
      classifiers=['Intended Audience :: Science/Research',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5'],
      )
