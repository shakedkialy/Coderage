import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.0'
PACKAGE_NAME = 'Coderage'
AUTHOR = 'Doron Lavi, Nitzan Drori, Shaked Kialy, Dor Itah, Tomer Ben Amos'
URL = 'https://github.com/shakedkialy/Coderage'

LICENSE = 'MIT'
DESCRIPTION = 'Coderage is a package that allows running tests and code coverage in comparison over time.'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'pytest',
      'pytest-cov',
      'pytest-html'
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=['Main'],
      entry_points={
                'console_scripts': [
                    'Coderage = Main.cmd:main',
                ],
            }
      )