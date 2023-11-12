from setuptools import setup

with open("./requirements.txt") as f:
    install_requires = f.read().splitlines()

setup(
    name="qmusix",
    version="1.0",
    install_requires=install_requires,
    # Other setup parameters
)
