import logging
import subprocess
import sys


logger = logging.getLogger(__name__)


def run_python_system_check() -> bool:
    check_result = subprocess.run(
        [sys.executable, "--version"],
        capture_output=True,
        text=True,
        check=False,
    )
    if check_result.returncode == 0:
        logger.info(
            "System check passed: %s",
            check_result.stdout.strip()
        )
        return True
    
    else:
        logger.error(
            "System check failed: %s",
            check_result.stderr.strip()
        )
        return False
        