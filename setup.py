from setuptools import setup, find_packages
import os

# Function to determine if the platform is Unix-like
def is_unix():
    return os.name == 'posix'

setup(
    name='bobByDew',
    version='1.0',
    packages=find_packages(),
    description='This Python package provides a real-time visualization of cryptocurrency order books from the Binance exchange. Utilizing asynchronous programming and WebSockets, it streams market depth data for BTC/USDT and calculates key trading metrics. The package features a terminal-based user interface created with the curses library to display bids, asks, spread, weighted averages, total volume, and order flow imbalance, updating dynamically to reflect live market conditions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Mr Dew',
    author_email='james@meeteden.dev',
    url='https://github.com/jamestylerboyd/bobByDew',
    install_requires=open('requirements.txt').read().splitlines(),
    # Specify the entry point for the script
    entry_points={
        'console_scripts': [
            'bobByDew=bobByDew:main',
        ],
    },
    # Set executable permissions only for Unix-like systems
    data_files=[('bin' if is_unix() else 'Scripts', ['bobByDew.py'])],
)
