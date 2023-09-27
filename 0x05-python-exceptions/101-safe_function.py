#!/usr/bin/python3

from sys import stderr

def safe_function(fct, *args):
    """Executes a function safely.

    Args:
        fct: The function to execute.
        args: Arguments for fct.

    Returns:
        If an error occurs - None.
        Otherwise - the result of the call to fct.
    """
    try:
        f = fct(*args)
        return (f)
    except Exception as err:
        print("Exception: {}".format(err), file=stderr)
        return (None)
