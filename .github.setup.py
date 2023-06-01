from setuptools import setup, Extension

import os
import platform

from distutils.core import setup, Extension


VERSION = "1.3.9"
DESC = """Python bindings for ILM's OpenEXR image file format.

This is a script to autobuild the wheels using github actions. Please, do not
use it manually

If you detect any problem, please feel free to report the issue on the GitHub
page:

https://github.com/sanguinariojoe/pip-openexr/issues
"""


libraries=['z']
libraries_static=['Iex-3_1', 'OpenEXR-3_1']

extra_compile_args = ['-DVERSION="%s"' % VERSION]
if platform.system() == 'Darwin':
    extra_compile_args += ['-std=c++11',
                           '-Wc++11-extensions',
                           '-Wc++11-long-long']

libraries_dir = "./openexr.install/lib"
if not os.path.isdir(libraries_dir):
    libraries_dir = "./openexr.install/lib64"
if platform.system() == "Windows":
    extra_link_args = [libraries_dir + lib + ".lib"
                       for lib in libraries_static]
    extra_link_args = extra_link_args + [
        "ws2_32.lib", "dbghelp.lib", "psapi.lib", "kernel32.lib", "user32.lib",
        "gdi32.lib", "winspool.lib", "shell32.lib", "ole32.lib",
        "oleaut32.lib", "uuid.lib", "comdlg32.lib", "advapi32.lib"]
else:
    extra_link_args = [libraries_dir + lib + ".a"
                       for lib in libraries_static]


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
              libraries=libraries,
              extra_compile_args=extra_compile_args,
              extra_link_args=extra_link_args,
              )
  ],
  py_modules=['Imath'],
)
