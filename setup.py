import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fortnox-python",
    version="0.0.1",
    author="Mahmudul Hasan",
    author_email="ikhtiarcse10ruet@gmail.com",
    description="A small package for Fortnox API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xalien10/fortnox-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
