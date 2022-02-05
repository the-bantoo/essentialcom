from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in essentialcom/__init__.py
from essentialcom import __version__ as version

setup(
	name="essentialcom",
	version=version,
	description="Essential Commodities Customisations",
	author="Bantoo",
	author_email="devs@thebantoo.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
