import requests
from .config import BASE_URL, HEADERS_JSON
from .endpoints import AUTH, BOOKING, PING


class ApiClient:
    def __init__(self, base_url: str = BASE_URL, default_headers: dict = None):
        self.base_url = base_url
        self.default_headers = default_headers or HEADERS_JSON.copy()

    def build_url(self, path: str) -> str:
        return f"{self.base_url}{path}"

    def post(self, path: str, json: dict = None, headers: dict = None, cookies: dict = None, auth: tuple = None):
        return requests.post(self.build_url(path), json=json, headers=headers or self.default_headers, cookies=cookies, auth=auth)

    def get(self, path: str, params: dict = None, headers: dict = None, cookies: dict = None):
        return requests.get(self.build_url(path), params=params, headers=headers or self.default_headers, cookies=cookies)

    def put(self, path: str, json: dict = None, headers: dict = None, cookies: dict = None, auth: tuple = None):
        return requests.put(self.build_url(path), json=json, headers=headers or self.default_headers, cookies=cookies, auth=auth)

    def delete(self, path: str, headers: dict = None, cookies: dict = None, auth: tuple = None):
        return requests.delete(self.build_url(path), headers=headers or self.default_headers, cookies=cookies, auth=auth)

    def create_token(self, payload: dict):
        return self.post(AUTH, json=payload)

    def create_booking(self, payload: dict):
        return self.post(BOOKING, json=payload)

    def get_booking(self, booking_id: int):
        return self.get(f"{BOOKING}/{booking_id}")

    def get_bookings(self, params: dict = None):
        return self.get(BOOKING, params=params)

    def update_booking(self, booking_id: int, payload: dict, cookies: dict = None, auth: tuple = None):
        return self.put(f"{BOOKING}/{booking_id}", json=payload, cookies=cookies, auth=auth)

    def delete_booking(self, booking_id: int, cookies: dict = None, auth: tuple = None):
        return self.delete(f"{BOOKING}/{booking_id}", cookies=cookies, auth=auth)

    def ping(self):
        return self.get(PING)
