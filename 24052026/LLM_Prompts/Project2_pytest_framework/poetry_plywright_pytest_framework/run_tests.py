from __future__ import annotations

import sys
import pytest


def main() -> int:
    print("==================================================")
    print("Starting Restful Booker API Automation Test Suite")
    print("==================================================")

    # Arguments to run pytest programmatically
    args = [
        "-v",
        "--html=reports/report.html",
        "--self-contained-html",
        "--alluredir=allure-results",
    ]

    # Run pytest
    exit_code = pytest.main(args)

    print("==================================================")
    print(f"Test run completed with exit code: {exit_code}")
    print("HTML Report generated at: reports/report.html")
    print("Allure results saved to: allure-results")
    print("==================================================")
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
