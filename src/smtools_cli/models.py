from pathlib import Path
from argparse import ArgumentParser


def build_parser() -> ArgumentParser:
    """Build and return the main CLI parser."""
    main_parser = ArgumentParser(
        prog="small_tools",
        description="Provides simple file utility functionalities.",
        allow_abbrev=False,
    )

    subparsers = main_parser.add_subparsers(dest="subcommands")

    # Directory size subcommand.
    dir_size_parser = subparsers.add_parser(
        "dir_size",
        aliases=["ds"],
        allow_abbrev=False,
        description=(
            "Computes and displays the size of a directory "
            "in a human readable format."
        ),
        help="Command to retrieve the size of a directory.",
    )

    dir_size_parser.add_argument(
        "dir_path",
        nargs="?",
        type=Path,
        default=Path.cwd(),
        help="Path to a directory. Defaults to cwd: %(default)s",
    )

    # Contains File subcommand.
    find_parser = subparsers.add_parser(
        "find",  # File in directory = find
        allow_abbrev=False,
        description="Useful for checking if a file with a particular name exists within a given directory.",
        help="Command to check if a file exists within a given directory.",
    )

    find_parser.add_argument(
        "--name",
        metavar="string",
        required=True,
        help="Name of a file.",
    )
    find_parser.add_argument(
        "--dir",
        dest="dir_path",
        default=Path.cwd(),
        type=Path,
        help="Path to directory. Defaults to cwd: %(default)s.",
        metavar="Path",
    )
    find_parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="If provided searches through the subdirectories.",
        dest="recursive",
    )

    # Contains Directory subcommand.
    dind_parser = subparsers.add_parser(
        "dind",  # Directory in directory = dind
        aliases=["dd"],
        allow_abbrev=False,
        description="Useful for checking if a directory with a particular name exists within a given directory.",
        help="Command to check if a directory exists within a given directory.",
    )

    dind_parser.add_argument(
        "--name", required=True, metavar="string", help="Name of a directory."
    )
    dind_parser.add_argument(
        "--dir",
        dest="dir_path",
        default=Path.cwd(),
        type=Path,
        help="Path to directory. Defaults to cwd: %(default)s.",
        metavar="Path",
    )
    dind_parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="If provided searches through the subdirectories.",
        dest="recursive",
    )

    return main_parser
