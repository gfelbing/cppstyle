from setuptools import setup

setup(
    name="cppstyle",
    version="0.0.3",
    description="Checks C/C++ code along an clang AST.",
    url="http://github.com/gfelbing/cppstyle",
    author="Georg Felbinger",
    author_email="gfelbing@github.com",
    license="GPLv3",
    packages=["cppstyle","cppstyle.model"],
    scripts=['bin/cppstyle'],
    zip_safe=False,
    install_requires=['argparse', 'pyyaml']
)
