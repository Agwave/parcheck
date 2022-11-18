import setuptools


with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

setuptools.setup(
    name="parcheck",
    version="0.1.1",
    author="Agwave",
    author_email="agwave@foxmail.com",
    description="A lightweight, minimalist, easy-to-use python toolkit",
    url="https://github.com/Agwave/parcheck.git",
    python_requires=">=3",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
)
