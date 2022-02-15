from distutils.core import setup
from distutils.extension import Extension
from distutils.command.build_py import build_py as _build_py

from os import system
import platform

from distutils.core import setup, Extension


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
    libraries=['Iex', 'Half', 'Imath', 'IlmImf', 'z']
else:
    libraries=['Iex', 'OpenEXR', 'z']

version = "1.3.7"
setup(name='OpenEXR',
  author = 'James Bowman',
  author_email = 'jamesb@excamera.com',
  url = 'https://github.com/sanguinariojoe/pip-openexr',
  description = "Python bindings for ILM's OpenEXR image file format",
  long_description = DESC,
  version=version,
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
              extra_compile_args=['-g', '-DVERSION="%s"' % version])
  ],
  py_modules=['Imath'],
)
