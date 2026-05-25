import subprocess
import sys

if __name__ == "__main__":
    command = [
        sys.executable,
        "-m",
        "pytest",
        "-q",
        "testcases",
        "--alluredir",
        "reports/allure-results",
    ]
    subprocess.run(command, check=True)
