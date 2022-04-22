<div align="center">

<h1>Board</h1>

[![Pytest](https://github.com/a5chin/awesome-board/actions/workflows/pytest.yml/badge.svg)](https://github.com/a5chin/awesome-board/actions/workflows/pytest.yml) [![Linting](https://github.com/a5chin/awesome-board/actions/workflows/linting.yml/badge.svg)](https://github.com/a5chin/awesome-board/actions/workflows/linting.yml) [![License](https://img.shields.io/pypi/l/ansicolortags.svg)](https://img.shields.io/pypi/l/ansicolortags.svg)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](examples/demo_savefig.ipynb)

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