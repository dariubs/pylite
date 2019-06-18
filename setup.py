import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pylite',
    version='0.1.0',
    description='Intract with sqlite3 in python as simple as it can be.',
    author='Dariush Abbasi',
    author_email='poshtehani@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://dariubs.github.io/pylite',
    packages=setuptools.find_packages(),
    package_dir={'pylite': 'pylite'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT'
)
