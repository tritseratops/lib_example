import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='lib_example',
    version='0.0.6',
    author='Horsa Gorbunchul',
    author_email='hb@gmail.com',
    description='Test lib to check how to include private libs',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/tritseratops/lib_example.git',
    project_urls = {
        "Main URL": "https://github.com/tritseratops/lib_example.git"
    },
    license='MIT',
    packages=['lib_example'],
    install_requires=['requests'],
)