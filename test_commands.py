import re
import subprocess

class TestCommandLineUtils:
    def test_mkdir(self, tmp_path):
        # Создание директории test_dir (mkdir test_dir)
        dir_path = tmp_path / "test_dir"
        subprocess.run(["mkdir", str(dir_path)], check=True)
        assert dir_path.exists(), "Созданный путь не существует"
        assert dir_path.is_dir(), "Название созданной директории не соответствует запрошенному"

    def test_mkdir_parents(self, tmp_path):
        # Создание директории test_dir/test_dir2 (mkdir -p test_dir2/test_dir3)
        dir_path = tmp_path / "test_dir2/test_dir3"
        subprocess.run(["mkdir", '-p', str(dir_path)], check=True)
        assert dir_path.exists(), "Созданный путь не существует"
        assert dir_path.is_dir(), "Название созданной директории не соответствует запрошенному"

    def test_mkdir_verbose(self, tmp_path):
        # Создание директории test_dir с выводом информации в консоль (mkdir -v test_dir)
        dir_path = tmp_path / "test_dir4"
        result = subprocess.run(["mkdir", '-v', str(dir_path)], capture_output=True, text=True, check=True)
        assert dir_path.exists(), "Созданный путь не существует"
        assert dir_path.is_dir(), "Название созданной директории не соответствует запрошенному"
        output = result.stdout.strip()
        pattern = re.escape(str(dir_path))
        assert re.search(pattern, output), f"Название созданной директории не выведено в консоль: {output}"

    def test_rmdir(self, tmp_path):
        # Удаление директории test_dir (rmdir test_dir)
        dir_path = tmp_path / "test_dir"
        dir_path.mkdir()
        subprocess.run(["rmdir", str(dir_path)], check=True)
        assert not dir_path.exists(), f"Созданная директория {dir_path} не удалена"

    def test_ls(self, tmp_path, capsys):
        # Обнаружение созданного файла при чтении содержимого директории (ls)
        dir_path = tmp_path / "test_dir"
        dir_path.mkdir()
        file_path = dir_path / "test_file.txt"
        file_path.write_text("Some text")
        result = subprocess.run(["ls", str(dir_path)], capture_output=True, text=True)
        assert "test_file.txt" in result.stdout, "test_file.txt не обнаружен в директории"

    def test_ls_hidden_not_visible(self, tmp_path, capsys):
        # Отсутствие созданного скрытого файла при чтении содержимого директории без специального ключа (ls)
        dir_path = tmp_path / "test_dir"
        dir_path.mkdir()
        file_path = dir_path / ".test_file.txt"
        file_path.write_text("Some text")
        result = subprocess.run(["ls", str(dir_path)], capture_output=True, text=True)
        assert not ".test_file.txt" in result.stdout, "скрытый файл test_file.txt виден в директории без использования специального ключа"

    def test_ls_hidden_is_visible(self, tmp_path, capsys):
        # Обнаружение созданного скрытого файла при чтении содержимого директории (ls -a)
        dir_path = tmp_path / "test_dir"
        dir_path.mkdir()
        file_path = dir_path / ".test_file.txt"
        file_path.write_text("Some text")
        result = subprocess.run(["ls", "-a", str(dir_path)], capture_output=True, text=True)
        assert ".test_file.txt" in result.stdout, "скрытый файл test_file.txt не виден в директории с использованием специального ключа"

    def test_cp(self, tmp_path):
        # Копирование файла (cp src.txt dest.txt)
        src_file = tmp_path / "src.txt"
        src_file.write_text("Some text")
        dest_file = tmp_path / "dest.txt"
        subprocess.run(["cp", str(src_file), str(dest_file)], check=True)
        assert dest_file.exists(), "файл dest.txt не существует"
        assert dest_file.read_text() == "Some text", "содержимое файла dest.txt не соответствует исходному"

    def test_cp_clobber(self, tmp_path):
        # Копирование файла без запрета на перезапись при существовании целевого файла (cp src.txt dest.txt&cp src2.txt dest.txt)
        src_file = tmp_path / "src.txt"
        src_file.write_text("Some text")
        src_file2 = tmp_path / "src2.txt"
        src_file2.write_text("Other text")
        dest_file = tmp_path / "dest.txt"
        subprocess.run(["cp", str(src_file), str(dest_file)], check=True)

        subprocess.run(["cp", str(src_file2), str(dest_file)], check=True)
        assert dest_file.exists(), "файл dest.txt не существует"
        assert dest_file.read_text() == "Other text", "содержимое файла dest.txt не перезаписано"

    def test_cp_no_clobber(self, tmp_path):
        # Копирование файла с запретом на перезапись при существовании целевого файла (cp src.txt dest.txt&cp -n src2.txt dest.txt)
        src_file = tmp_path / "src.txt"
        src_file.write_text("Some text")
        src_file2 = tmp_path / "src2.txt"
        src_file2.write_text("Other text")
        dest_file = tmp_path / "dest.txt"
        subprocess.run(["cp", str(src_file), str(dest_file)], check=True)

        subprocess.run(["cp", "-n", str(src_file2), str(dest_file)], check=True)
        assert dest_file.exists(), "файл dest.txt не существует"
        assert dest_file.read_text() == "Some text", "содержимое файла dest.txt перезаписано"

