from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    description = fh.read()

setup(
    name="BanglaLanguageToolkit",
    version="0.2",
    packages=find_packages(include=['BanglaLanguageToolkit', 'BanglaLanguageToolkit.*']),
    install_requires=[
        "ftfy==6.1.1",
        "emoji==1.4.2",
    ],
    long_description=description,
    long_description_content_type="text/markdown",
)