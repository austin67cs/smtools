from smtools import tools
from pathlib import Path

def test_contains_dir():
    path = Path(__file__).parent
    
    assert tools.contains_dir(path, path.parent)

    # A directory cannot contain itself.
    assert not tools.contains_dir(path, path)

def test_recursively():
    """
    Assert that you can check if a given file exists anywhere within a given directory.
    """
    path = Path(__file__).parent
    dir_path = path.parent.parent

    assert tools.contains_dir(path, dir_path, recursive=True)
    assert not tools.contains_dir(path, dir_path, recursive=False)
