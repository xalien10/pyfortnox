import pkg_resources
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as requirement:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirement)
    ]

setuptools.setup(
    name="pyfortnox",
    version="1.2.0",
    author="Mahmudul Hasan",
    author_email="ikhtiarcse10ruet@gmail.com",
    description="Fortnox API V3 library client for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xalien10/pyfortnox",
    packages=setuptools.find_packages(
        exclude=[
            'tests', 'tests.*',
        ]
    ),
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
    platforms='any',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
