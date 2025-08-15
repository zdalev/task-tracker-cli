from task_tracker.cli import make_cli
from task_tracker.flows.add_flow import add_flow_run
from task_tracker.flows.delete_flow import delete_flow_run
from task_tracker.flows.mark_flow import mark_flow_run
from task_tracker.flows.update_flow import update_flow_run

from task_tracker.logger import get_logger, setup_logging
from task_tracker.tasks import TasksRepo

logger = get_logger(__name__)

# Note: create file/folder that contain constants
OPTION_FLOWS = {"add": add_flow_run,
                "update": update_flow_run,
                "delete": delete_flow_run,
                "mark": mark_flow_run,
                "list": lambda x: x, }

OPTIONS = ["add", "update", "delete", "mark", "list"]


def main():
    repo = TasksRepo()
    arguments = make_cli()
    setup_logging(arguments.log_level.upper())
    logger.info("starting the process")
    logger.debug(f"Passed arguments: {arguments}")

    for option in OPTIONS:
        args_attr = getattr(arguments, option)
        if args_attr:
            logger.info(f"Entering in the {option.upper()} flow")
            OPTION_FLOWS.get(option)(repo, args_attr)
