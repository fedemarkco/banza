from fastapi.testclient import TestClient

from app.config import settings
from app.config.db_testing import app


class TestCaseCategory:
    def setup(self):
        self.client = TestClient(app)

    def test_create_category(self):
        """
        Check create a new categoria
        Return status code 200
        """
        data_category = {"name": "Category 1"}

        response = self.client.post(
            f"{settings.API_V1_STR}/category/", json=data_category
        )

        assert response.status_code == 200
        assert response.json() == {"id": 1, "name": "Category 1"}

    def test_client_to_category(self):
        """
        Check adding an client to a categoría
        Return status code 200
        """
        data_client = {"name": "Client 1"}

        data_category = {"id_category": 1, "id_client": 1}

        self.client.post(f"{settings.API_V1_STR}/client/", json=data_client)
        response = self.client.post(
            f"{settings.API_V1_STR}/client_to_category/", json=data_category
        )

        assert response.status_code == 200
        assert response.json() == {"id": 1, "id_client": 1, "id_category": 1}
