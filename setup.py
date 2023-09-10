from setuptools import setup, find_packages

setup(
    name="BanglaLanguageToolkit",
    version="0.1",
    packages=find_packages(include=['BanglaLanguageToolkit', 'BanglaLanguageToolkit.*']),
    install_requires=[
        "ftfy==6.1.1",
        "emoji==1.4.2",
    ],
)