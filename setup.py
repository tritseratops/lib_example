import pathlib
import setuptools

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.rst").read_text()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='lib_example',
    version='0.0.9',
    author='Horsa Gorbunchul',
    author_email='hb@gmail.com',
    description='Test lib to check how to include private libs',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    # url='https://github.com/tritseratops/lib_example.git',
    project_urls = {
        "Main URL": "https://github.com/tritseratops/lib_example.git"
    },
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python"
    ],
    packages=setuptools.find_packages(),
    # packages=['lib_example'],
    # install_requires=['requests'],
    python_requires=">=3"
)