from setuptools import setup, find_packages
from pathlib import Path
import datetime

Path("demo.txt").write_text(
    f"setup.py executed at {datetime.datetime.now().isoformat()}\n"
)

setup(
    name="demo_pkg",
    version="0.0.1",
    packages=find_packages(),
)
