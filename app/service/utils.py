import requests

from app.config import settings
from app.models import MovementEnum


class AccountBalance:
    def get_total_usd(self):
        dolar_amount = "-"
        try:
            response = requests.get(settings.DOLARSI, timeout=15)
            if response.status_code == 200:
                for data in response.json():
                    if data["casa"]["nombre"].lower() == "dolar bolsa":
                        dolar_amount = float(data["casa"]["venta"].replace(",", "."))
        except Exception:
            dolar_amount = "Page not working"

        return dolar_amount

    def balance(self, movements):
        total_amount = 0
        for movement in movements:
            if movement.type == MovementEnum.DEPOSIT:
                total_amount += movement.amount
            if movement.type == MovementEnum.WITHDRAWAL:
                total_amount -= movement.amount

        dolar_amount = self.get_total_usd()
        if type(dolar_amount) != str:
            dolar_amount *= total_amount

        return total_amount, dolar_amount
