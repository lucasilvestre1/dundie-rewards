import argparse
from dundie.core import load


def main():
    parser = argparse.ArgumentParser(
        description="Dunder Mifflin Rewards CLI",
        epilog="Enjoy and for any doubts read the documentation"
    )
    parser.add_argument(
        "subcommand",
        type=str,
        help="The subcommand/function to run",
        choices=("load", "view", "send"),
        default="help",
    )
    parser.add_argument(
        "filepath",
        type=str,
        help="File path to load",
        default=None,
    )
    args = parser.parse_args()
    print('\n'.join(globals()[args.subcommand](args.filepath)))

