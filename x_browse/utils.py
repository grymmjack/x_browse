import os
import rich
import collections

from rich import print


class log_types:
    ERROR = -1
    WARNING = 0
    NOTICE = 1


def path_to_file(path):
    """Returns file cursor for relative path string
        Args:
            path (str): The path name to the file
        Returns:
            str: The relative path to the file
    """
    return os.path.join(os.path.dirname(__file__), path)


def log(message, log_type=log_types.NOTICE):
    """ Create a log message, and output it using print
    In this case, print is overriden to use rich libraries
    print method to afford formatting, color, etc.
    Args:
        message (str): The message to log
        log_type(log_types[int]): Type of log message
    Returns:
        None
    """
    if log_type == log_types.ERROR:
        parsed_message = f"[bold red]{message}[/]"
    elif log_type == log_types.WARNING:
        parsed_message = f"[bold yellow]{message}[/]"
    else:
        parsed_message = f"{message}"
    print(parsed_message)
