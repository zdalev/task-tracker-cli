import argparse
from typing import Any


def verify_mark_argument(values):
    if len(values) != 2:
        raise argparse.ArgumentTypeError("Exactly 2 arguments required: <status> <task>")

    status, task = values
    choices = ["in-progress", "done", "todo"]

    if status not in choices:
        raise argparse.ArgumentTypeError(f"FAILED: argument -m/--mark: invalid choice: 'in-progres' "
                                         f"(choose from 'in-progress', 'done', 'todo')")
    if task in choices:
        raise argparse.ArgumentTypeError(f"Second argument cannot be one of {choices}")

def make_cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Base task tracker cli.",
                                     usage='use "%(prog)s --help" for more information',
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-a",
                        "--add",
                        type=str,
                        help="Add new task into the tracker.")

    parser.add_argument("-u",
                        "--update",
                        nargs='+',
                        help="Update specified task into the tracker.")
    parser.add_argument("-d",
                        "--delete",
                        type=int,
                        help="Delete specified task into the tracker.")
    parser.add_argument("-m",
                        "--mark",
                        type=str,
                        nargs=2,
                        help="Change specified task progress into the tracker. Viable options: in-progress, done, todo")
    parser.add_argument("-l",
                        "--list",
                        type=str,
                        default=None,
                        help="List all or specified tasks based on status from the tracker.")
    parser.add_argument("-log",
                        "--log-level",
                        default="INFO",
                        help=argparse.SUPPRESS,
                        )

    args = parser.parse_args()

    if args.mark:
        try:
            verify_mark_argument(args.mark)
        except argparse.ArgumentTypeError as e:
            print(e)
            exit()
    return args
