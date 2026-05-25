from __future__ import annotations

import time
import concurrent.futures
import allure
import pytest

from framework.fluent_api import Given
from framework.logger import get_logger

logger = get_logger("NonFunctionalTests")


@allure.feature("Non-Functional Testing")
@pytest.mark.non_functional
class TestNonFunctional:

    @allure.story("Availability / HealthCheck")
    @allure.title("TC-NF008: Verify ping health check endpoint is available and responsive")
    def test_health_check_ping(self, api: Given) -> None:
        # Restful-booker returns HTTP 201 Created for GET /ping
        start_time = time.perf_counter()
        api.when().get("/ping") \
           .then().status_code(201) \
           .body_contains("Created")
        duration = (time.perf_counter() - start_time) * 1000
        logger.info(f"Health check response time: {duration:.2f} ms")
        allure.attach(f"{duration:.2f} ms", name="Ping Response Time", attachment_type=allure.attachment_type.TEXT)

    @allure.story("Performance - GET Latency")
    @allure.title("TC-NF001: Measure and record response time distribution for read operations")
    def test_performance_get_booking_latency(self, api: Given) -> None:
        latencies = []
        for i in range(10):
            start = time.perf_counter()
            api.when().get("/booking") \
               .then().status_code(200)
            latencies.append((time.perf_counter() - start) * 1000)

        min_lat = min(latencies)
        max_lat = max(latencies)
        avg_lat = sum(latencies) / len(latencies)

        summary_msg = f"GET /booking latency (10 requests) - Min: {min_lat:.2f}ms, Max: {max_lat:.2f}ms, Avg: {avg_lat:.2f}ms"
        logger.info(summary_msg)
        allure.attach(summary_msg, name="GET Performance Summary", attachment_type=allure.attachment_type.TEXT)

    @allure.story("Performance - POST Latency")
    @allure.title("TC-NF002: Measure and record response times for create operations")
    def test_performance_post_booking_latency(self, api: Given, load_payload) -> None:
        payload = load_payload("create_booking.json")
        latencies = []
        for i in range(5):
            payload["firstname"] = f"PerfUser{i}"
            start = time.perf_counter()
            api.body(payload) \
               .when().post("/booking") \
               .then().status_code(200)
            latencies.append((time.perf_counter() - start) * 1000)

        min_lat = min(latencies)
        max_lat = max(latencies)
        avg_lat = sum(latencies) / len(latencies)

        summary_msg = f"POST /booking latency (5 requests) - Min: {min_lat:.2f}ms, Max: {max_lat:.2f}ms, Avg: {avg_lat:.2f}ms"
        logger.info(summary_msg)
        allure.attach(summary_msg, name="POST Performance Summary", attachment_type=allure.attachment_type.TEXT)

    @allure.story("Concurrency - Concurrent Reads")
    @allure.title("TC-NF006 / TC-NF003: Measure API behavior under concurrent requests")
    def test_concurrency_measurement(self, api: Given) -> None:
        # Define worker for thread execution
        def make_request(worker_id: int) -> float:
            start = time.perf_counter()
            try:
                # Use subcontext fetch inside thread if needed, but since we are measuring, we use our Given spec
                api.when().get("/booking") \
                   .then().status_code(200)
                return (time.perf_counter() - start) * 1000
            except Exception as e:
                logger.error(f"Thread worker {worker_id} failed: {e}")
                return -1.0

        num_threads = 5
        logger.info(f"Launching {num_threads} concurrent GET requests")
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = [executor.submit(make_request, i) for i in range(num_threads)]
            results = [f.result() for f in concurrent.futures.as_completed(futures)]

        successful_results = [r for r in results if r > 0]
        failures = results.count(-1.0)
        avg_latency = sum(successful_results) / len(successful_results) if successful_results else 0.0

        summary = f"Concurrency Results ({num_threads} workers) - Success: {len(successful_results)}, Failures: {failures}, Avg Latency: {avg_latency:.2f}ms"
        logger.info(summary)
        allure.attach(summary, name="Concurrency Test Results", attachment_type=allure.attachment_type.TEXT)

    @allure.story("Security - HTTPS Enforcement")
    @allure.title("TC-NF009: Verify TLS / HTTPS secure connection enforcement")
    def test_security_https_enforcement(self, api_config) -> None:
        # Check that base URL is configured with HTTPS
        assert api_config.base_url.startswith("https://"), f"Base URL {api_config.base_url} does not enforce HTTPS/TLS!"
        logger.info(f"Verified base URL uses secure protocol: {api_config.base_url}")
        allure.attach(f"Base URL: {api_config.base_url}", name="HTTPS Protocol Verification", attachment_type=allure.attachment_type.TEXT)

    @allure.story("Security - Authorization Enforcement")
    @allure.title("TC-NF010: Verify authorization requirements for protected endpoints")
    def test_security_auth_enforcement_details(self, api: Given, load_payload) -> None:
        # Test PUT without token
        payload_update = load_payload("update_booking.json")
        api.body(payload_update) \
           .when().put("/booking/1") \
           .then().status_code(403)

        # Test DELETE without token
        api.when().delete("/booking/1") \
           .then().status_code(403)

    @allure.story("Rate Limiting")
    @allure.title("TC-NF007: Rate Limiting behavior observation")
    def test_rate_limiting_observation(self) -> None:
        # The spec contains no documented rate limits, so this is a placeholder measurement-only report.
        logger.info("Observed: No documented rate limits in the API Specification. Rate limiting is measurement-only.")
        allure.attach("No documented rate limits in API Spec.", name="Rate Limiting Assessment", attachment_type=allure.attachment_type.TEXT)

    @allure.story("Backup & Recovery")
    @allure.title("TC-NF011: Backup & Recovery measurement attempt")
    def test_backup_and_recovery_attempt(self) -> None:
        # No backup/recovery API exists in the Restful Booker spec.
        # We record that there is insufficient information.
        logger.info("Observed: Insufficient information to proceed with Backup & Recovery testing (no API or process documented in Spec).")
        allure.attach("No backup/recovery endpoints or details documented in API Spec.", name="Backup & Recovery Assessment", attachment_type=allure.attachment_type.TEXT)
