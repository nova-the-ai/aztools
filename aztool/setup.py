# setup.py
from setuptools import setup, find_packages

setup(
    name='aztool',  # Package name
    version='0.1.1',  # Version
    packages=find_packages(),  # Automatically discover all packages
    install_requires=[],  # Add dependencies if needed, e.g., ['requests']
    author='NOVA',  # Replace with your name
    description='A custom tool to greet and fetch Wi-Fi (hotspot) details.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum Python version
    entry_points={
        'console_scripts': [
            'aztool-greet=aztool.core:greet',
            'aztool-wifi=aztool.core:get_wifi_details'
        ],
    },
)
