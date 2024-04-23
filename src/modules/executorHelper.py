# executorHelper.py
def check_verbose(args):
    # Check if verbose is set via command-line arguments
    return '-v' in args or '--verbose' in args
