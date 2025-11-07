from setuptools import setup, find_packages

setup(
    name='data-science-project',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A basic data science project structure',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your project dependencies here
    ],
)