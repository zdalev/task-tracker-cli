from task_tracker.cli import make_cli

from task_tracker.logger import get_logger

logger = get_logger(__name__)


def main():
    logger.info("starting the process")
    arguments = make_cli()

    logger.setLevel(arguments.log_level)
    logger.debug(f"Passed arguments: {arguments}")
