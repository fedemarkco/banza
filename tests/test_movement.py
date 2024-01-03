from fastapi.testclient import TestClient
from app.config.db_testing import app
from app.config import settings
from app.models.constants import MovementEnum


class TestCaseCategory:
    def setup(self):
        self.client = TestClient(app)

    def test_create_movement(self):
        """
        Check create a movement
        If the client wants to withdraw and there is no balance, return status code 403
        If the client wants to deposit, a movement will be generated, return status code 200
        """
        data_client = {
            "name": "Client 1"
        }

        data_account = {
            "id_client": 1
        }

        data_category_client = {
            "id_account": 1,
            "type": MovementEnum.WITHDRAWAL,
            "amount": 5
        }

        self.client.post(f"{settings.API_V1_STR}/client/", json=data_client)
        self.client.post(f"{settings.API_V1_STR}/account_to_client/", json=data_account)

        response = self.client.post(f"{settings.API_V1_STR}/movement/", json=data_category_client)

        assert response.status_code == 403
        assert response.json()["detail"] == "insufficient balance"

        data_category_client = {
            "id_account": 1,
            "type": MovementEnum.DEPOSIT,
            "amount": 5
        }

        response = self.client.post(f"{settings.API_V1_STR}/movement/", json=data_category_client)

        assert response.status_code == 200
        assert data_category_client.items() <= response.json().items()

    def test_get_movement(self):
        """
        Check to obtain the movement of a client
        Return status code 200
        """
        response = self.client.get(f"{settings.API_V1_STR}/movement/1/1/")

        assert response.status_code == 200
        assert response.json()["id"] == 1
        assert response.json()["amount"] == 5
        assert response.json()["type"] == MovementEnum.DEPOSIT

    def test_delete_movement(self):
        """
        Check delete a client
        Return status code 200
        The query of the deleted movement will obtain status code 404
        """
        response = self.client.delete(f"{settings.API_V1_STR}/movement/1")

        assert response.status_code == 200

        response = self.client.get(f"{settings.API_V1_STR}/movement/1/1/")

        assert response.status_code == 404
        assert response.json()["detail"] == "Movement or Account not found"
