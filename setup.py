from distutils.core import setup
from distutils.extension import Extension
from distutils.command.build_py import build_py as _build_py

from os import system
import platform

from distutils.core import setup, Extension


VERSION = "1.3.9"
DESC = """Python bindings for ILM's OpenEXR image file format.

To install this packge, make sure your system already has the OpenEXR library
installed before.

If you detect any problem, please feel free to report the issue on the GitHub
page:

https://github.com/sanguinariojoe/pip-openexr/issues
"""


print("Looking for libOpenEXR...")
if platform.system() == "Linux" and system("ldconfig -p | grep libOpenEXR"):
    # There is no libOpenEXR, probably an old version of OpenEXR
    libraries=['Iex', 'Imath', 'z']
else:
    libraries=['Iex', 'OpenEXR', 'z']

extra_compile_args = ['-g', '-DVERSION="%s"' % VERSION]
if platform.system() == 'Darwin':
    extra_compile_args += ['-std=c++11',
                           '-Wc++11-extensions',
                           '-Wc++11-long-long']

setup(name='OpenEXR',
  author = 'James Bowman',
  author_email = 'jamesb@excamera.com',
  url = 'https://github.com/sanguinariojoe/pip-openexr',
  description = "Python bindings for ILM's OpenEXR image file format",
  long_description = DESC,
  version=VERSION,
  ext_modules=[ 
    Extension('OpenEXR',
              ['OpenEXR.cpp'],
              include_dirs=['/usr/include/OpenEXR',
                            '/usr/local/include/OpenEXR',
                            '/opt/local/include/OpenEXR',
                            '/usr/include/Imath',
                            '/usr/local/include/Imath',
                            '/opt/local/include/Imath'],
              library_dirs=['/usr/lib',
                            '/usr/local/lib',
                            '/opt/local/lib'],
              libraries=libraries,
              extra_compile_args=extra_compile_args)
  ],
  py_modules=['Imath'],
)
