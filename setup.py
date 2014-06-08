from setuptools import setup, find_packages

setup(
    name="serename",
    version="0.0.1-dev",
    description="",
    long_description="",
    author="Ruben Smets",
    packages=find_packages(),
    install_requires=open("requirements.txt").readlines(),
    test_suite="serename.test.suite"
)