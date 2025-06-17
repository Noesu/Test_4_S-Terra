from pathlib import Path


def file_exists(_, file_name: str, output: str) -> (bool, str):
    """Verify if filename exists in command output.
    Args:
        _: Unused path parameter (kept for interface consistency)
        file_name: Filename to search for in output
        output: Command output string to search in
    """
    exists: bool = file_name in output
    message: str = f"file {file_name} exists in output" if exists else f"file {file_name} not exists in output"
    return exists, message

def dir_exists(path: Path, dir_name: str, _) -> (bool, str):
    """Verify if directory exists in filesystem.
    Args:
        path: Base path to check in
        dir_name: Directory name to check
        _: Unused output parameter (kept for interface consistency)
    """
    exists: bool = (path / dir_name).exists()
    message: str = f"directory {dir_name} exists" if exists else f"directory {dir_name} not exists"
    return exists, message

def is_directory(path: Path, dir_name: str, _) -> (bool, str):
    """Verify if the path object is a directory.
    Args:
        path: Base path to check in
        dir_name: Directory name to verify
        _: Unused output parameter"""
    is_dir: bool = (path / dir_name).is_dir()
    message: str = f"object {dir_name} is directory" if is_dir else f"object {dir_name} is not a directory"
    return is_dir, message
