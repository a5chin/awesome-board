import sys
from pathlib import Path

import numpy as np
import pytest
from torch.utils.tensorboard import SummaryWriter

current_dir = Path(__file__).resolve().parent
sys.path.append(str(current_dir) + "/../")

from board import Board


@pytest.mark.parametrize(
    ("log_dir", "output_dir", "freq"), [("./logs", "./outputs", 100)]
)
def test_board(log_dir, output_dir, freq):
    random = np.random.randn(freq)
    writer = SummaryWriter(log_dir=log_dir)
    board = Board(log_dir=log_dir)

    for i in range(freq):
        writer.add_scalar("random", random[i], i)

    board.savefig(output_dir=output_dir)

    assert True
