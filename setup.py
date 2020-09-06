import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyfortnox",
    version="1.2.0",
    author="Mahmudul Hasan",
    author_email="ikhtiarcse10ruet@gmail.com",
    description="Fortnox API V3 library client for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xalien10/pyfortnox",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["munch>=2.5.0", "requests>=2.21.0", "urllib3>=1.24.3", "requests-toolbelt>= 0.9.1"],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
