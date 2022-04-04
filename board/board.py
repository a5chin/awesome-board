import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from typing import Dict
from pathlib import Path
from tensorboard.backend.event_processing.event_accumulator import EventAccumulator


class Board:
    WALL_TIME = 0
    STEP = 1
    VALUE = 2

    def __init__(self, log_dir: str) -> None:
        self.log_files = [path for path in Path(log_dir).iterdir() if path.is_file()]
        self.scalars = self.get_scalars()

    def get_scalars(self) -> Dict:
        data = {log_file.stem: {} for log_file in self.log_files}

        for log_file in self.log_files:
            event = EventAccumulator(str(log_file))
            event.Reload()

            tags = event.Tags()["scalars"]

            for tag in tags:
                scalars = event.Scalars(tag)
                data[log_file.stem][tag] = []

                for scalar in scalars:
                    data[log_file.stem][tag].append(scalar[Board.VALUE])

        return data

    def savefig(self, output_dir: str, extention: str="png") -> None:
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        for file in self.scalars.keys():
            for tag in self.scalars[file].keys():
                df = pd.DataFrame(self.scalars[file][tag])

                df.plot(kind="line", title=tag, legend=False)
                plt.savefig(f"{output_dir}/{file}_{tag}.{extention}")
                plt.close()

