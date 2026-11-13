import requests


class NexusClient:
    def __init__(self, base_url="http://127.0.0.1:8000"):
        self.base_url = base_url.rstrip("/")
        self.token = None

    def login(self, email, password):
        response = requests.post(
            f"{self.base_url}/api/v1/auth/login",
            data={"username": email, "password": password}
        )
        response.raise_for_status()
        self.token = response.json()["token"]
        return response.json()

    def request(self, method, endpoint, **kwargs):
        headers = kwargs.pop("headers", {})
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        response = requests.request(
            method,
            f"{self.base_url}{endpoint}",
            headers=headers,
            **kwargs
        )
        response.raise_for_status()
        return response.json() if response.content else {}
