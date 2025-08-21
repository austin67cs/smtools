from smtools import tools
from pathlib import Path
import pytest, string, random


def test_get_size():
    """
    Test for correctness.
    Assert that the size of a directory is same as the sum of the sizes of all files therein.
    """

    direc = Path.cwd()

    size = sum(path.stat().st_size for path in direc.rglob("*") if path.is_file())

    assert size == tools.get_dir_size(direc)


def test_argu():
    """
    Test that argument is a valid directory.
    """

    path = Path(__file__)
    with pytest.raises(NotADirectoryError):
        """
        Test that when called with a file raises a NotADirectoryError.
        """
        tools.get_dir_size(path)

    rand_string = "".join(random.choices(string.ascii_lowercase, k=5))
    path = path.with_stem(rand_string)
    with pytest.raises(NotADirectoryError):
        """
        Test that when called with a non existing path raises a NotADirectoryError.
        """
        if not path.exists():
            tools.get_dir_size(path)
