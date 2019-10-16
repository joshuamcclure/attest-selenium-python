# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from setuptools import find_packages, setup
import subprocess

with open("./README.rst") as f:
    readme = f.read()

from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install


class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        #develop.run(self)
        cmd = "npm install"
        returned_value = subprocess.call(cmd, shell=True)
        print('returned value:', returned_value)

setup(
    cmdclass={
        'develop': PostDevelopCommand,
    },
    name="attest-selenium-python",
    use_scm_version=True,
    description="Python library to integrate Attest HTML and selenium for web \
                accessibility testing.",
    long_description=open("README.rst").read(),
    url="https://github.com/joshuamcclure/attest-selenium-python",
    author="Joshua McClure",
    author_email="joshua.mcclure@deque.com",
    install_requires=["selenium>=3.0.2", "pytest>=3.0"],
    license="Mozilla Public License 2.0 (MPL 2.0)",
    keywords="axe-core selenium pytest-selenium accessibility automation mozilla",
)