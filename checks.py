def file_exists(_, param, output):
    """Проверяет, содержится ли имя файла в выводе команды"""
    result = param in output
    return result, f"файл {param} присутствует в выводе" if result else f"файл {param} отсутствует в выводе"

def dir_exists(path, param, _):
    """Проверяет, существует ли директория"""
    result = (path / param).exists()
    return result, f"объект {param} существует" if result else f"объект {param} не существует"

def is_directory(path, param, _):
    """Проверяет, является ли путь директорией"""
    result = (path / param).is_dir()
    return result, f"объект {param} является директорией" if result else f"объект {param} не является директорией"
