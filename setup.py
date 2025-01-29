def create_file(path, file_name):
    """Создаёт файл с содержимым"""
    (path / file_name).write_text("Some text")
    return f"создан файл {file_name}"

def create_directory(path, dir_name):
    """Создаёт директорию"""
    (path / dir_name).mkdir()
    return f"создана директория {dir_name}"
