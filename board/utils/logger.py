import logging
from typing import Optional


class Logger:
    def __init__(self, log_file: Optional[str] = None) -> None:
        self.fmt = logging.Formatter(
            fmt="[%(asctime)s] :%(name)s: [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        handler = logging.StreamHandler()
        handler.setFormatter(self.fmt)
        self.logger.addHandler(handler)

        if log_file is not None:
            handler = logging.FileHandler(log_file)
            handler.setFormatter(self.fmt)
            self.logger.addHandler(handler)

    def log(self, message: str) -> None:
        self.logger.info(message)
