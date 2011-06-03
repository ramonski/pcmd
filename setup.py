from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='pcmd',
      version=version,
      description="Runs Shell Commands in the parent Shell (MAC only)",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='Mac Terminal Python Shell Appscript',
      author='Ramon Bartl',
      author_email='ramon_bartl@yahoo.de',
      url='https://github.com/ramonski/pcmd',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          "appscript"
      ],
      entry_points={
          'console_scripts': [
              'p=pcmd:main',
              ],
          },
      )
