from setuptools import setup, find_packages

setup(
    name="serename",
    version="0.0.1-dev",
    description="Python command line tool to batch rename tv shows.",
    long_description="",
    author="Ruben Smets",
    packages=find_packages(exclude=['test']),
    install_requires=open("requirements.txt").readlines(),
    test_suite="serename.test.suite"
)
