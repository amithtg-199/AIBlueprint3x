# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains multiple QA/testing focused projects and educational materials:
- **AITesterBlueprint3x**: Main educational blueprint with chapters on LLM fundamentals and prompt engineering for QA
- **LLM_Prompts/Project2_pytest_framework**: Python pytest API testing framework for Restful Booker service
- **poetry_pytest_example**: Python API automation framework using Playwright and pytest with Poetry dependency management

## Common Development Commands

### For the Restful Booker PyTest Framework (`LLM_Prompts/Project2_pytest_framework/Restful-booker-py-framework/`):
```bash
# Install dependencies
python -m pip install -r requirements.txt

# Run all tests
python run_tests.py
# or
pytest -q

# Run with Docker
docker build -t restful-booker-tests .
docker run --rm restful-booker-tests

# Run specific test markers
pytest -m "smoke" -v
```

### For the Playwright API Testing Framework (`poetry_pytest_example/AI-Engineering/RestAssuredApiTestingFrameWork/`):
```bash
# Install dependencies
poetry install

# Run tests
poetry run pytest

# Generate HTML report
poetry run pytest --html=reports/api-report.html --self-contained-html
```

### For the Selenium Framework (`AITesterBlueprint3x/chapter_02_Prompt_Eng/Project2_Selenium_Framework/AdvanceSeleniumFramework/`):
```bash
# Compile and run tests
mvn -q clean test-compile
mvn test                       # full suite
mvn test -DsuiteXmlFile=testng-smoke.xml   # smoke only
```

## Code Architecture & Structure

### Restful Booker PyTest Framework
- **framework/**: Shared modules (`api_client.py`, `config.py`, `data_loader.py`, `endpoints.py`, `utils.py`)
- **testcases/**: Organized test cases (`happy/` for positive scenarios, `negative/` for negative tests)
- **resources/data/**: JSON test data files
- **conftest.py**: Pytest fixtures for test data loading
- **run_tests.py**: Simple entrypoint script
- **pytest.ini**: Configuration with `testpaths = testcases`

### Playwright API Automation Framework
- **framework/**: Fluent API client, request specifications, response validators, logging utilities
- **tests/**: pytest API test suites using Playwright's APIRequestContext
- **test_data/**: JSON payloads and test case documentation
- Uses Poetry for dependency management with environment-specific configuration

### Educational Projects (AITesterBlueprint3x)
- **chapter_01_LLM_Basics**: Foundational LLM/Transformer concepts with interactive visualizations
- **chapter_02_Prompt_Eng**: 
  - Anti-hallucination rules for QA prompts
  - RICE-POT framework (Role, Instructions, Context, Example, Parameters, Output, Tone)
  - Project 1: Test case generation from PRD/API docs
  - Project 2: Selenium framework generation from prompts
  - Reusable prompt templates for common QA tasks

## Key Patterns & Conventions

1. **Test Data Management**: Both Python frameworks externalize test data to JSON files (`resources/data/functional_test_data.json` and `test_data/` directories respectively)

2. **Configuration**: Use of dedicated config modules/files for environment-specific settings (URLs, timeouts, etc.)

3. **Modular Design**: Separation of concerns with API clients, utilities, and test cases in distinct modules

4. **Fixture Usage**: Pytest fixtures in `conftest.py` for shared setup/teardown and data loading

5. **Documentation**: Each test case or framework includes associated markdown documentation

## Working with Prompts & Templates

The repository includes various prompt templates for QA work:
- Anti-hallucination rules to constrain LLM outputs
- RICE-POT framework templates for structured prompting
- Specific templates for test case generation, API testing, negative tests, security tests, and regression suites

These templates are designed to be copy-pasted into LLMs with specific sections replaced for the task at hand.

## Running Specific Tests

To run individual tests or test groups:
```bash
# Run a specific test file
pytest testcases/happy/test_tc_f002_create_booking.py -v

# Run tests by marker
pytest -m "auth" -v

# Run negative tests only
pytest testcases/negative/ -v

# Run with verbose output and capture disabled
pytest -v -s
```