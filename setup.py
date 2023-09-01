from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erptech_account/__init__.py
from erptech_account import __version__ as version

setup(
	name="erptech_account",
	version=version,
	description="new account which overweight Account module",
	author="erptech",
	author_email="erptechin@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
