import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zoom-joiner-mithun-sri", # Replace with your own username
    version="1.0",
    author="Mithun Sri",
    author_email="lnsmirth@gmail.com",
    description="A package to fetch and join zoom meetings automatically",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mithun-sri/zoom-joiner",
    packages=setuptools.find_packages(exclude=['ez_setup', 'examples', 'tests']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,

)
