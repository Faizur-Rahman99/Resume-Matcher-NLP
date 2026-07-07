from setuptools import find_packages, setup

setup(
    name="ResumeMatcher",
    version="0.0.1",
    author="Faizur Rahman",
    author_email="faizurrahmanayeen99@gmail.com",
    packages=find_packages(),
    install_requires=[],
)

from src.utils.download_nltk import *

print("Project setup completed.")