import os
requirementPath = "requirements.txt"
install_requires = []

if os.path.isfile(requirementPath):
      with open(requirementPath) as f:
            install_requires = f.read().splitlines()

from setuptools import setup, find_packages
setup(
      name = "OpMath",
      version = "0.1",
      description = "OpMath Distribution Package",
      packages = find_packages(),
      include_packages_data = True,
      install_requires = install.requires,
      entry_points = {
            "console_scripts":[
                  "OpMath = OpMath.cli: main"
            ]
      }

)