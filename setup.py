from setuptools import setup 
from setuptools import find_packages

setup(
  name='gcode2xyz',
  version='0.0.1-1', # use semantic version conventions
  packages= ['gcode2xyz'],
  license='MIT',
  long_description=open('README.md').read(),
  install_requires=[],
  entry_points = {
   'console_scripts': [
     'gcode2xyz = gcode2xyz.cli:main',          
   ]
  },
  author = "Kyle Heath",
  author_email = "heathkh@gmail.com",
  description = "A utility to convert gcode generated by slic3r into a 3w file for the XYZ davinci 3d printer.",
  keywords = ""    
)
