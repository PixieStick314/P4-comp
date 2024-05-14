# executorHelper.py
def check_verbose(args):
    # Check if verbose is set via command-line arguments
    return '-v' in args or '--verbose' in args


def check_script_path(args):
    # Check if script path is parsed as arg
    return '-p' in args or '--path' in args
