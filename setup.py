from setuptools import setup, find_packages

setup(
    name="pytest-suite-timeout",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pytest>=6.0",
    ],
    entry_points={
        "pytest11": [
            "suite-timeout = pytest_suite_timeout.plugin",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
)
