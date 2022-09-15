from setuptools import find_packages, setup

from board.version import __version__

setup(
    name="board",
    version=__version__,
    description="Tools for visualising TensorBoard outputs.",
    url="https://github.com/a5chin/board",
    author="a5chin",
    license="MIT",
    install_requires=[
        "pandas",
        "matplotlib",
        "seaborn",
        "tensorboard",
    ],
    packages=find_packages(),
    python_requires=">=3.7",
)
