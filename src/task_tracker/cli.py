import argparse


def make_cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Base task tracker cli.")

    parser.add_argument("-a",
                        "--add",
                        type=str,
                        help="Add new task into the tracker.")

    parser.add_argument("-u",
                        "--update",
                        type=int,
                        help="Update specified task into the tracker.")
    parser.add_argument("-d",
                        "--delete",
                        type=int,
                        help="Delete specified task into the tracker.")
    parser.add_argument("-m",
                        "--mark",
                        type=int,
                        help="Change specified task progress into the tracker.")
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
    return args
