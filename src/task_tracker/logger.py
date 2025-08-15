import logging
import sys

def setup_logging(level: str = 'INFO'):
    """Configure logging once for the whole project."""
    logging.basicConfig(
        level=level,
        format="[%(asctime)s] [%(levelname)s] %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

def get_logger(name: str):
    """Get a logger with the given name."""
    return logging.getLogger(name)