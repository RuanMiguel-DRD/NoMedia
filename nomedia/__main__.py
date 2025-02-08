#!/usr/bin/env python3

from argparse import ArgumentParser, Namespace

from os import getcwd, remove, path
from pathlib import Path


arguments = ArgumentParser(
    prog="NoMedia",
    description="Hides the indicated folders from the cell phone's media",
    epilog="https://github.com/RuanMiguel-DRD/NoMedia"
)

arguments.add_argument(
    "directory",
    help="defines which directory will be hidden from the media",
    default=getcwd(),
    nargs="?"
)

arguments.add_argument(
    "-r",
    "--recursive",
    action="store_true",
    help="work in all subfolders from the indicated directory"
)

arguments.add_argument(
    "-u",
    "--unhide",
    action="store_true",
    help="unhide the media directory"
)


def main():
    """Main program execution"""

    argument: Namespace = arguments.parse_args()

    directory: str = argument.directory
    recursive: bool = argument.recursive
    unhide: bool = argument.unhide

    if check_directory(directory):

        target_list = [Path(directory).resolve()]

        if recursive:
            visited = set()

            for path in target_list[0].rglob("*"):

                if path.is_dir():
                    real_path = path.resolve()

                    if real_path not in visited:
                        visited.add(real_path)
                        target_list.append(str(path))

        error: str | None

        for target in target_list:
            error = media_control(target, unhide)

            if error != None:
                print(error)

    else:
        print("Error: No valid directory provided")


def check_directory(directory: Path | str) -> bool:
    """Checks if a valid directory path was provided"""

    if not path.isdir(directory):
        return False

    return True


def media_control(directory: Path | str, unhide: bool = False) -> bool:
    """Controls the visibility of a folder in the media
    
    There is no need to test whether the received directory
    is valid internally in the function, as the validation is
    already done previously during the execution of the program."""

    file = Path(f"{directory}/.nomedia")

    try:
        if file.is_dir():
            return f"Error: There is a directory named \".nomedia\" inside \"{directory}\""

        if unhide:
            if path.exists(file):
                remove(file)

        else:
            open(file, "w").close()

        return None

    except (PermissionError):
        return f"Error: You do not have sufficient permissions to work on directory \"{directory}\""


if __name__ == "__main__":
    main()
