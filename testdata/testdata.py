from utils.checks import file_exists, dir_exists, is_directory
from utils.setup import create_file, create_directory


TST_DIR = "test_dir"
TST_SUBDIR = "test_dir/test_dir2"
TST_FILE = "test_file.txt"
HIDDEN_FILE = ".test_file.txt"
TST_FILE2 = "test_file2.txt"

"""
СТРУКТУРА ДАННЫХ ДЛЯ ТЕСТА:
    команда, параметры,
    (команды подготовки тестовой среды),
    (тесты результата выполнения команды)
"""

testdata = [
    (
        ("mkdir", TST_DIR,),
        (),
        (
            (dir_exists, TST_DIR, True, f"Directory {TST_DIR} doesn`t exists"),
            (is_directory, TST_DIR, True, f"Object {TST_DIR} is not a directory"),
        ),
    ),
    (
        ("mkdir", "-p", TST_SUBDIR,),
        (),
        (
            (dir_exists, TST_SUBDIR, True, f"Directory {TST_SUBDIR} doesn`t exists"),
            (is_directory, TST_SUBDIR, True, f"Object {TST_SUBDIR} is not a directory"),
        ),
    ),
    (
        ("mkdir", TST_SUBDIR,),
        (),
        (
            (dir_exists, TST_SUBDIR, False, f"Directory {TST_SUBDIR} doesn`t exists"),
        ),
    ),
    (
        ("rmdir", TST_DIR,),
        (
            (create_directory, TST_DIR,),
        ),
        (
            (dir_exists, TST_DIR, False, "Directory wasn`t deleted"),
        ),
    ),
    (
        ("ls",),
        (
            (create_file, TST_FILE,),
        ),
        (
            (file_exists, TST_FILE, True, f"{TST_FILE} not found"),
        ),
    ),
    (
        ("ls",),
        (
            (create_file, HIDDEN_FILE),
        ),
        (
            (file_exists, HIDDEN_FILE, False, f"{HIDDEN_FILE} is visible without '-a' key"),
        ),
    ),
]
