import logging
from pathlib import Path
from typing import Dict

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from tensorboard.backend.event_processing.event_accumulator import EventAccumulator

sns.set()


class Board:
    WALL_TIME = 0
    STEP = 1
    VALUE = 2

    def __init__(self, log_dir: str) -> None:
        self.log_files = [path for path in Path(log_dir).glob("**/*") if path.is_file()]
        self.scalars = self.get_scalars()
        self._logger = get_logger()

    def get_scalars(self) -> Dict:
        data = {log_file.parent.name: {} for log_file in self.log_files}

        for log_file in self.log_files:
            event = EventAccumulator(str(log_file))
            event.Reload()

            tags = event.Tags()["scalars"]

            for tag in tags:
                scalars = event.Scalars(tag)
                data[log_file.parent.name][tag] = []

                for scalar in scalars:
                    data[log_file.parent.name][tag].append(scalar[Board.VALUE])

        return data

    def savefig(self, output_dir: str, extension: str = "png") -> None:
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        for file in self.scalars.keys():
            for tag in self.scalars[file].keys():
                df = pd.DataFrame(self.scalars[file][tag])

                df.plot(kind="line", title=tag, legend=False)
                plt.savefig(f"{output_dir}/{file}_{tag}.{extension}")
                plt.close()

                self._logger.info(f"{file}/{tag} saved.")


def get_logger() -> logging.Logger:
    fmt = logging.Formatter(
        fmt="[%(asctime)s] :%(name)s: [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    handler.setFormatter(fmt)

    logger.addHandler(handler)

    return logger
