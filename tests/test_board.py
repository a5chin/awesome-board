import numpy as np
from torch.utils.tensorboard import SummaryWriter

from board import Board


NUM = 100
LOG_DIR = "./logs"
OUT_DIR = "./outputs"

def test_board():
    random = np.random.randn(NUM)
    writer = SummaryWriter(log_dir=LOG_DIR)
    board = Board(log_dir=LOG_DIR)

    for i in range(NUM):
        writer.add_scalar("random", random[i], i)

    board.savefig(output_dir=OUT_DIR)

    assert True
