from fastapi.testclient import TestClient

from app.config import settings
from app.config.db_testing import app


class TestCaseAccount:
    def setup(self):
        self.client = TestClient(app)

    def test_account_to_client(self):
        """
        Check adding an account to a client
        Return status code 200
        """
        data_client = {"name": "Client 1"}

        data_account = {"id_client": 1}

        self.client.post(f"{settings.API_V1_STR}/client/", json=data_client)
        self.client.post(f"{settings.API_V1_STR}/account_to_client/", json=data_account)

        response = self.client.get(f"{settings.API_V1_STR}/client_info/1/")

        assert response.status_code == 200
        assert response.json() == {
            "client": {"id": 1, "name": "Client 1"},
            "accounts": [1],
            "categories": [],
        }
