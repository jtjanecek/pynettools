import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pynettools",
    version="0.0.1",
    author="John Janecek",
    author_email="janecektyler@gmail.com",
    description="Python networking tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jtjanecek/pynettools",
    project_urls={
        "Bug Tracker": "https://github.com/jtjanecek/pynettools/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
	install_requires=[],
	packages=setuptools.find_packages(),
    python_requires=">=3.7",
)
