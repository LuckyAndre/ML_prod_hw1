from setuptools import find_packages, setup

setup(
    name="ml_project",
    packages=find_packages(),
    version="0.1.0",
    description="Example of ml project",
    author="Andrei Belenko",
    install_requires=[
        "notebook == 6.3.0",
        "pandas == 1.2.4",
        "pandas-profiling == 3.0.0",
        "click == 7.0"
    ]
)