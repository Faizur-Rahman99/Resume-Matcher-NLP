from setuptools import find_packages, setup

setup(
    name="resume-matcher-nlp",
    version="1.0.0",
    author="Faizur Rahman",
    author_email="faizurrahmanayeen99@gmail.com",
    description="AI-powered Resume Matcher using NLP, FastAPI, Streamlit, and Sentence Transformers.",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.11",
)