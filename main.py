

# 1-m_isol
import random
import datetime
from decimal import Decimal

class Temperature:
    def __init__(self):
        self._harorat = None
        self._timestamp = None

    def set_temperature(self):
        temp = random.uniform(-10, 40)
        if temp < -50 or temp > 50:
            raise ValueError("Harorat me'yordan chiqib ketdi!")
        self._harorat = Decimal(str(temp))
        self._timestamp = datetime.datetime.now()

    @property
    def harorar(self):
        return f"Harorat: {self._harorat}°C ({self._timestamp.strftime('%Y-%m-%d')})"


temp = Temperature()
temp.set_temperature()
print(temp.harorar)

# 3-misol
from decimal import Decimal
import datetime

class chipta_narhi:
    def __init__(self, narx):
        try:
            self._price = Decimal(str(narx))
        except InvalidOperation:
            raise ValueError("Chipta narxi noto‘g‘ri")
        self._sales_date = datetime.datetime.now()

    @property
    def ticket_info(self):
        return f"Chipta narxi: {self._price} UZS. Sotish sanasi: {self._sales_date.strftime('%Y-%m-%d')}"


chipta = chipta_narhi(15000)
print(chipta.ticket_info)

# 4-misol
from decimal import Decimal
import datetime
class Oylik_ish_haqi:
    def __init__(self, ish_haqi):
        try:
            self._ishhaqi = Decimal(str(ish_haqi))
        except InvalidOperation:
            raise ValueError("Maosh noto‘g‘ri formatda!")
        self._payment_date = datetime.datetime.now()

    @property
    def salary_info(self):
        return f"Ishchi oyligi: {self._ishhaqi} UZS. To‘lov sanasi: {self._payment_date.strftime('%Y-%m-%d')}"

# Misol
salary = Oylik_ish_haqi(3200000)
print(salary.salary_info)
