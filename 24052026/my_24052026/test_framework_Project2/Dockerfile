FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY Restful-booker-py-framework ./Restful-booker-py-framework
COPY testcases ./testcases
COPY pytest.ini ./pytest.ini
COPY run_tests.py ./run_tests.py

ENV PYTHONPATH="/app/Restful-booker-py-framework"

ENTRYPOINT ["python", "run_tests.py"]
