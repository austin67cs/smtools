import pytest, random, string
from smtools import tools
from pathlib import Path

rand_string = lambda: "".join(random.choices(string.ascii_lowercase, k=5))

def test_contains_file():
    path = Path(__file__)
    
    assert tools.contains_file(path)

def test_recursively():
    """
    Assert that you can check if a given file exists anywhere within a given directory.
    """
    path = Path(__file__)
    dir_path = path.parent.parent

    assert tools.contains_file(path, dir_path, recursive=True)


def test_argu():
    """
    Test that only valid file and directory paths are passed.
    """
    file_path = Path(__file__)
    with pytest.raises(NotADirectoryError):
        """
        Test that only a valid directory path is passed to dir parameter.
        """
        # Passing a valid file path to the dir parameter raises NotADirectoryError.
        tools.contains_file(file_path, file_path, recursive=True)

    with pytest.raises(NotADirectoryError):
        # Passing an invalid directory path to file parameter raises NotADirectoryError.
        dir_path = Path.cwd() / rand_string()
        tools.contains_file(file_path, dir_path, recursive=True)

    dir_path = file_path.parent
    with pytest.raises(ValueError):
        """
        Test that only a valid file path is passed to the file parameter.
        """
        # Passing a valid directory path to the file parameter raises ValueError.
        tools.contains_file(dir_path, dir_path, recursive=False)

    with pytest.raises(ValueError):
        # Passing an invalid file path to the file parameter raises ValueError.
        file_path = Path.cwd() / rand_string()
        tools.contains_file(file_path)
        