from setuptools import setup

setup(
    name="pocketses",
    description="What has it got in its pocketses, precious?!",
    version="0.1",
    url="https://snapcraft.io/pocketses",
    author="Stephen Mwangi",
    license="MIT",
    python_requires=">=3.10",
    packages=["pocketses"],
    entry_points={
        "console_scripts": ["pocketses-cli=pocketses.main:main"],
    },
)
