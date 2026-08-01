# Restful-booker-py-framework

## Project structure

- `Dockerfile` - container image definition for running the tests.
- `pytest.ini` - pytest configuration with `testpaths = testcases`.
- `requirements.txt` - Python dependencies required by the test suite.
- `run_tests.py` - simple entrypoint script that executes `pytest`.
- `framework/` - shared test framework modules.
  - `api_client.py` - API wrapper for the Restful Booker service.
  - `config.py` - static configuration and URLs used by tests.
  - `data_loader.py` - loads test data from JSON.
  - `endpoints.py` - API endpoint definitions.
  - `utils.py` - helper utilities.
- `resources/data/functional_test_data.json` - test input data for booking and auth scenarios.
- `testcases/` - actual pytest tests.
  - `conftest.py` - fixtures used by tests.
  - `happy/` - positive scenario tests.
  - `negative/` - negative scenario tests.

## How to specify test data

Test data is stored in `resources/data/functional_test_data.json`.
The test fixture in `testcases/conftest.py` reads this JSON and exposes it as `test_data`.

Example structure:

```json
{
  "auth_valid": {
    "username": "admin",
    "password": "password123"
  },
  "booking_valid": {
    "firstname": "John",
    "lastname": "Doe",
    "totalprice": 123,
    "depositpaid": true,
    "bookingdates": {
      "checkin": "2025-01-01",
      "checkout": "2025-01-05"
    },
    "additionalneeds": "Breakfast"
  }
}
```

To add or update data:
1. Edit `resources/data/functional_test_data.json`.
2. Update the test cases or fixtures to consume any new keys.

## How to execute tests locally

From the `Restful-booker-py-framework` directory:

```bash
python -m pip install -r requirements.txt
python run_tests.py
```

Or run pytest directly:

```bash
pytest -q
```

## How to use Docker

Build the Docker image:

```bash
docker build -t restful-booker-tests .
```

Run the tests in Docker:

```bash
docker run --rm restful-booker-tests
```

If you need to mount live data from the host, use:

```bash
docker run --rm -v "$(pwd)/resources:/app/resources:ro" restful-booker-tests
```

## Docker Compose

This repository includes `docker-compose.yaml` for local execution and CI orchestration.

Run with:

```bash
docker compose up --build --abort-on-container-exit
```

Bring down the service:

```bash
docker compose down
```

## CI/CD usage

Use the Dockerfile in your pipeline to build and run the test image.

Example CI steps:

1. Checkout repository.
2. Build image:

```bash
docker build -t restful-booker-tests .
```

3. Run tests:

```bash
docker run --rm restful-booker-tests
```

For pipeline systems that support Docker Compose, run:

```bash
docker compose up --build --abort-on-container-exit
```

## GitHub Actions

A GitHub Actions workflow is included at the repository path:

```text
.github/workflows/restful-booker-tests.yml
```

This workflow triggers on push or pull request when files under `24052026/my_24052026/test_framework_Project2/Restful-booker-py-framework/**` change.

It performs:
1. checkout
2. Python 3.12 setup
3. Docker image build
4. test execution inside `restful-booker-tests`

If you want, I can also add test reporting or artifact upload to this workflow.
``