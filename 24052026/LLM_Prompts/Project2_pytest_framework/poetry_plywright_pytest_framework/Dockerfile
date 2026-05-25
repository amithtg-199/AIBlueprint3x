FROM python:3.10-slim

WORKDIR /app

# Install system dependencies needed for Playwright
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy project specification files
COPY pyproject.toml poetry.lock* /app/

# Configure Poetry to not create a virtual environment
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Install Playwright system dependencies (if running browsers is needed, though not strictly required for APIRequestContext, we still run the install command to ensure it's available)
RUN playwright install --with-deps

# Copy rest of the files
COPY . /app

# Run poetry installation for root package
RUN poetry install --no-interaction --no-ansi

CMD ["poetry", "run", "python", "run_tests.py"]
