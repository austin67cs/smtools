from pathlib import Path


def format_size(size: int) -> str:
    """
    Format a file size in bytes into a human-readable string
    (bytes, KB, MB, GB, or TB).
    """
    for unit in ("bytes", "KB", "MB", "GB", "TB"):
        if size < 1024 or unit == "TB":
            return f"{size:.8f} {unit}"
        size /= 1024


def get_dir_size(dir_path: Path) -> int:
    """
    Return the total size of a directory in bytes,
    including all files in subdirectories.
    """
    # Pre-condition: dir_path must be path to a directory only.
    if not dir_path.is_dir():
        raise NotADirectoryError(f"dir_path: {dir_path} is not a valid directory.")
    
    return sum(path.stat().st_size for path in dir_path.rglob("*") if path.is_file())


def contains_file(file: Path, dir: Path = Path.cwd(), recursive: bool = False) -> bool:
    """
    Return True if the given file is located within the specified directory.

    Args:
        file (Path): Path to the file to check.
        dir (Path): Directory to search (defaults to current working directory).
        recursive (bool): If True, search within all subdirectories.

    Returns:
        bool: True if the file lives in the directory (or its subdirectories when
              recursive=True), otherwise False.

    Raises:
        ValueError: If `file` does not exist or is not a file.
        NotADirectoryError: If `dir` does not exist or is not a directory.
    """
    if not file.exists() or not file.is_file():
        raise ValueError(f"{file} is not a valid file path.")
    if not dir.exists() or not dir.is_dir():
        raise NotADirectoryError(f"{dir} is not a valid directory path.")

    if recursive:
        return dir.resolve() in file.resolve().parents
    return file.parent.resolve() == dir.resolve()


def contains_dir(
    sub_dir: Path, dir: Path = Path.cwd(), recursive: bool = False
) -> bool:
    """
    Return True if the given subdirectory is located within the specified directory.

    Args:
        sub_dir (Path): The directory to check.
        dir (Path): The parent directory to search (defaults to current working directory).
        recursive (bool): If True, search within all nested subdirectories.

    Returns:
        bool: True if `sub_dir` is directly inside `dir` (or within it when
              recursive=True), otherwise False.

    Raises:
        NotADirectoryError: If `sub_dir` is not a valid directory.
        NotADirectoryError: If `dir` is not a valid directory.
    """
    if not sub_dir.exists() or not sub_dir.is_dir():
        raise NotADirectoryError(f"{sub_dir} is not a valid directory path.")

    if not dir.exists() or not dir.is_dir():
        raise NotADirectoryError(f"{dir} is not a valid directory path.")

    if recursive:
        return dir.resolve() in sub_dir.resolve().parents
    return sub_dir.parent.resolve() == dir.resolve()


def get_path(path: Path | str) -> Path:
    path = Path(path) if type(path) == str else path
    return path.resolve()


def get_files_with_name(
    name: str, dir_path: Path = Path.cwd(), recursive: bool = False
):
    """
    Return a sequence of file paths whose names match the given name within the specified directory.

    Args:
        name (str): Name of file to check.
        dir (Path): Directory to search (defaults to current working directory).
        recursive (bool): If True, search within all subdirectories.

    Returns:
        Generator[Path | None]
    """

    if recursive:
        for path in dir_path.rglob("*"):
            if path.is_file() and path.name == name:
                yield path

    else:
        file = Path(name)
        if file.exists():
            yield file.resolve()


def get_dirs_with_name(name: str, dir_path: Path = Path.cwd(), recursive: bool = False):
    """
    Return a sequence of directory paths whose names match the given name within the specified directory.

    Args:
        name (str): Name of file to check.
        dir (Path): Directory to search (defaults to current working directory).
        recursive (bool): If True, search within all subdirectories.

    Returns:
        Generator[Path | None]
    """
    if recursive:
        for path in dir_path.rglob("*"):
            if path.is_dir() and path.name == name:
                yield path

    else:
        directory = Path(name)
        if directory.exists():
            yield directory.resolve()
