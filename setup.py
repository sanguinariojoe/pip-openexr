import platform
from setuptools import setup, Extension
from os import system

VERSION_MAJOR = 1
VERSION_MINOR = 3
VERSION_PATCH = 10
VERSION = f"{VERSION_MAJOR}.{VERSION_MINOR}.{VERSION_PATCH}"
DESC = """Python bindings for ILM's OpenEXR image file format.

To install this package, make sure your system already has the OpenEXR library
installed before.

If you detect any problem, please feel free to report the issue on the GitHub
page:

https://github.com/sanguinariojoe/pip-openexr/issues
"""


print("Looking for libOpenEXR...")
if platform.system() == "Linux" and system("ldconfig -p | grep libOpenEXR"):
    # There is no libOpenEXR, probably an old version of OpenEXR
    libraries = ["Iex", "Half", "Imath", "IlmImf", "z"]
else:
    libraries = ["Iex", "OpenEXR", "z"]

include_dirs = [
    "/usr/include/OpenEXR",
    "/usr/local/include/OpenEXR",
    "/opt/local/include/OpenEXR",
    "/usr/include/Imath",
    "/usr/local/include/Imath",
    "/opt/local/include/Imath",
]

library_dirs = [
    "/usr/lib",
    "/usr/local/lib",
    "/opt/local/lib",
    "/opt/homebrew/opt/openexr/lib",
    "/opt/homebrew/opt/imath/lib",
]

definitions = [
    ("PYOPENEXR_VERSION_MAJOR", f"{VERSION_MAJOR}"),
    ("PYOPENEXR_VERSION_MINOR", f"{VERSION_MINOR}"),
    ("PYOPENEXR_VERSION_PATCH", f"{VERSION_PATCH}"),
]
extra_compile_args = []
if platform.system() == "Darwin":
    extra_compile_args += ["-std=c++11", "-Wc++11-extensions", "-Wc++11-long-long"]
    include_dirs += [
        "/opt/homebrew/opt/openexr/include/OpenEXR",
        "/opt/homebrew/opt/imath/include/Imath",
    ]
    library_dirs += ["/opt/homebrew/opt/openexr/lib", "/opt/homebrew/opt/imath/lib"]
if platform.system() == "Windows":
    include_dirs += [
        "C:/Program Files (x86)/OpenEXR/include/Imath",
        "C:/Program Files (x86)/OpenEXR/include/OpenEXR",
    ]
    library_dirs += [
        "C:/Program Files (x86)/OpenEXR/lib",
        "C:/Program Files/zlib/lib"
    ]
if "CONDA_PREFIX" in os.environ:  # override or append conda prefix
    libraries = ["Iex", "OpenEXR", "z"]  # assume recent enough version
    include_dirs += [
        os.environ["CONDA_PREFIX"] + "/include/OpenEXR",
        os.environ["CONDA_PREFIX"] + "/include/Imath"
    ]
    library_dirs += [os.environ["CONDA_PREFIX"] + "/lib"]

setup(
    name="OpenEXR",
    author="James Bowman",
    author_email="jamesb@excamera.com",
    url="https://github.com/sanguinariojoe/pip-openexr",
    description="Python bindings for ILM's OpenEXR image file format",
    long_description=DESC,
    version=VERSION,
    ext_modules=[
        Extension(
            "OpenEXR",
            ["OpenEXR.cpp"],
            language="c++",
            define_macros=definitions,
            include_dirs=include_dirs,
            library_dirs=library_dirs,
            libraries=libraries,
            extra_compile_args=extra_compile_args,
        )
    ],
    py_modules=["Imath"],
)
