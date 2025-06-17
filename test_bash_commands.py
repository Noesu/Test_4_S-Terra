import logging
import subprocess

import pytest

from testdata.testdata import testdata


logger = logging.getLogger(__name__)

@pytest.mark.parametrize("command, setups, asserts", testdata)
def test_commands(tmp_path, command, setups, asserts):
    """Test shell commands with environment setup and result verification."""
    # Environment setup
    if setups:
        for setup_func, param in setups:
            setup_func(tmp_path, param)

    # Command execution
    full_command = " ".join(command)
    logger.info(f'Executing: {full_command}')
    try:
        result = subprocess.run(
            full_command,
            shell=True,
            check=True,
            capture_output=True,
            text=True,
            cwd=tmp_path
        )
        output = result.stdout.strip()
        logger.info(f'Command output: {output or "No output"}')
    except subprocess.CalledProcessError as e:
        output = e.stderr.strip()
        logger.warning(f'Command failed: {output}')

    # Result verification
    for check_func, param, expected, error_msg in asserts:
        result, check_msg = check_func(tmp_path, param, output)
        logger.info(f'Verification: {check_msg}')
        assert result == expected, error_msg
