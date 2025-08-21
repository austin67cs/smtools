from smtools import tools
from . import models

# TODO: Add support for use of regular expressions in file and directory lookup.


def main():
    parser = models.build_parser()
    args = parser.parse_args()

    match args.subcommands:
        case "dir_size" | "ds":
            size = tools.get_dir_size(tools.get_path(args.dir_path))
            print(tools.format_size(size))

        case "find":
            for file in tools.get_files_with_name(
                args.name, args.dir_path, args.recursive
            ):
                print(file)

        case "dind" | "dd":
            for path in tools.get_dirs_with_name(
                args.name, args.dir_path, args.recursive
            ):
                print(path)

        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
