import logging
import os


class Logger:

    @staticmethod
    def get_logger():

        os.makedirs("logs", exist_ok=True)

        logger = logging.getLogger("TichiAutomation")
        logger.setLevel(logging.INFO)

        # Remove existing handlers
        if logger.hasHandlers():
            logger.handlers.clear()

        file_handler = logging.FileHandler(
            "logs/automation.log",
            mode="a",
            encoding="utf-8"
        )

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        return logger