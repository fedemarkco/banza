from fastapi.testclient import TestClient

from app.config import settings
from app.config.db_testing import app


class TestCaseClient:
    def setup(self):
        self.client = TestClient(app)

    def test_create_client(self):
        """
        Check create a new client
        Return status code 200
        """
        data = {"name": "New Client"}

        response = self.client.post(f"{settings.API_V1_STR}/client/", json=data)

        assert response.status_code == 200
        assert response.json()["name"] == "New Client"

    def test_edit_client(self):
        """
        Check edit a client
        Return status code 200
        """
        data = {"name": "Client 2"}

        response = self.client.patch(f"{settings.API_V1_STR}/client/1/", json=data)

        assert response.status_code == 200
        assert response.json() == {"id": 1, "name": "Client 2"}

    def test_list_clients(self):
        """
        Check to get a list of clients
        Return status code 200
        """
        response = self.client.get(f"{settings.API_V1_STR}/clients/")

        assert response.status_code == 200
        assert len(response.json()) > 0

    def test_client_info(self):
        """
        Check to obtain client information
        Return status code 200
        """
        data_account = {"id_client": 1}

        data_category = {"name": "Category 1"}

        data_category_client = {"id_category": 1, "id_client": 1}

        self.client.post(f"{settings.API_V1_STR}/category/", json=data_category)
        self.client.post(
            f"{settings.API_V1_STR}/client_to_category/", json=data_category_client
        )
        self.client.post(f"{settings.API_V1_STR}/account_to_client/", json=data_account)

        response = self.client.get(f"{settings.API_V1_STR}/client_info/1/")

        assert response.status_code == 200
        assert "client" in response.json()
        assert "accounts" in response.json()
        assert "categories" in response.json()

    def test_client_balance(self):
        """
        Check to obtain the client balance
        Return status code 200
        """
        response = self.client.get(f"{settings.API_V1_STR}/client_balance/1/")

        assert response.status_code == 200
        assert "balance" in response.json()
        assert "id_account" in response.json()["balance"][0]
        assert "amount_pesos" in response.json()["balance"][0]
        assert "amount_dolar" in response.json()["balance"][0]

    def test_delete_client(self):
        """
        Check delete a client
        Return status code 200
        """
        response = self.client.delete(f"{settings.API_V1_STR}/client/1/")

        assert response.status_code == 200

        response = self.client.get(f"{settings.API_V1_STR}/client_balance/1/")

        assert response.status_code == 404
        assert response.json()["detail"] == "Client not found"
