from __future__ import annotations

import allure
import pytest

from framework.fluent_api import Given


@allure.feature("Authentication")
@pytest.mark.valid
class TestAuthSuccess:
    @allure.story("Create Auth Token - Happy Path")
    @allure.title("TC-F001: Verify successful Token creation with valid credentials")
    def test_create_token_success(self, api: Given, load_payload) -> None:
        payload = load_payload("auth_payload.json")

        api.body(payload) \
           .when().post("/auth") \
           .then().status_code(200) \
           .json_path_matches("token", lambda val: isinstance(val, str) and len(val) > 0)


@allure.feature("Authentication")
@pytest.mark.invalid
class TestAuthNegative:
    @allure.story("Create Auth Token - Invalid Credentials")
    @allure.title("TC-F001-Neg1: Verify token creation is rejected with invalid password")
    def test_create_token_invalid_password(self, api: Given) -> None:
        payload = {
            "username": "admin",
            "password": "wrongpassword"
        }

        # Restful-booker returns HTTP 200 with {"reason": "Bad credentials"} for invalid credentials
        api.body(payload) \
           .when().post("/auth") \
           .then().status_code(200) \
           .json_path("reason", "Bad credentials")

    @allure.story("Create Auth Token - Missing Fields")
    @allure.title("TC-F001-Neg2: Verify token creation is rejected when username is missing")
    def test_create_token_missing_username(self, api: Given) -> None:
        payload = {
            "password": "password123"
        }

        # Restful-booker returns HTTP 200 with {"reason": "Bad credentials"} for missing fields
        api.body(payload) \
           .when().post("/auth") \
           .then().status_code(200) \
           .json_path("reason", "Bad credentials")

    @allure.story("Create Auth Token - Missing Fields")
    @allure.title("TC-F001-Neg3: Verify token creation is rejected when password is missing")
    def test_create_token_missing_password(self, api: Given) -> None:
        payload = {
            "username": "admin"
        }

        api.body(payload) \
           .when().post("/auth") \
           .then().status_code(200) \
           .json_path("reason", "Bad credentials")
