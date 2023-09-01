from setuptools import setup, find_packages

setup(
    name="bangla_text_cleaner",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "ftfy==6.1.1",
        "emoji==1.4.2",
    ],
)