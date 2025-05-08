from setuptools import setup, find_packages

setup(
    name="pytest-suite-timeout",  # Name of the package
    version="0.1.0",  # Version number
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=[  # List of dependencies (if any)
        "pytest>=6.0",
    ],
    entry_points={  # Tell pytest to load the plugin
        "pytest11": [
            "suite-timeout = pytest_suite_timeout.plugin",
        ],
    },
    classifiers=[  # Optional classifiers for your package
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
)
