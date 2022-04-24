<div align="center">

<h1>Board</h1>

[![Pytest](https://github.com/a5chin/awesome-board/actions/workflows/pytest.yml/badge.svg)](https://github.com/a5chin/awesome-board/actions/workflows/pytest.yml) [![Linting](https://github.com/a5chin/awesome-board/actions/workflows/linting.yml/badge.svg)](https://github.com/a5chin/awesome-board/actions/workflows/linting.yml) [![License](https://img.shields.io/pypi/l/ansicolortags.svg)](https://img.shields.io/pypi/l/ansicolortags.svg)

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/) [![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)](examples/classification.ipynb) [![Numpy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)

</div>

## Usage

### Installation
```bash
pip install -r requirements.txt
```
or
```bash
pip install git+https://github.com/a5chin/awesome-board
```

### Example
```bash
from board import Board


board = Board("logs")
board.savefig("outputs", extension="png")
```

<img alt="learning rate in training NN" src="assets/images/log.png" width="100%">