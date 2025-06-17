import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def create_file(path: Path, file_name: str) -> None:
    """Create file with default content.
    Args:
        path: Path object where file will be created
        file_name: Name of the file to create
    Returns:
        str: Confirmation message with filename"""
    (path / file_name).write_text("Some text")
    logger.info(f"Setup test environment: File created {file_name}")

def create_directory(path: Path, dir_name: str) -> None:
    """Create a directory in the specified path.
    Args:
        path: Path object or string where directory should be created
        dir_name: Name of the directory to create
    Returns:
        str: Confirmation message with directory name
    """
    (path / dir_name).mkdir()
    logger.info(f"Setup test environment: Directory created {dir_name}")
