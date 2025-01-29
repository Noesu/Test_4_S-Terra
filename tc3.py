import pytest
import subprocess
from testdata import testdata


class TestCommand:
    @pytest.mark.parametrize("command, setups, asserts", testdata)
    def test_commands(self, tmp_path, command, setups, asserts):

        print(f'\nТестирование {command[0]}')
        command = " ".join(command)

        # Подготовка тестовой среды
        if setups:
            for setup, param in setups:
                message = setup(tmp_path, param)
                print(f'Подготовка тестовой среды: {message}')
        else:
            print('Без подготовки тестовой среды')
        print(f'Выполняется команда: {command}')

        # Выполнение команды
        try:
            output = subprocess.run(command, shell=True, check=True, capture_output=True, text=True,
                                    cwd=tmp_path).stdout.strip()
            print(f'Ответ системы: {output or "отсутствует"}')
        except subprocess.CalledProcessError as e:
            output = e.stderr.strip()
            print(f"Ошибка: {output}")

        # Проверка результата
        for check, param, expected_result, error_message in asserts:
            result, message = check(tmp_path, param, output)
            print(f'Проверка: {message}')  # Выводим сообщение
            assert result == expected_result, error_message
