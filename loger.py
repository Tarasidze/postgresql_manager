import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s]: %(message)s",
    handlers=[
        logging.FileHandler("logging.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
