from datetime import datetime


class Plan:
    def __init__(self, data) -> None:
        self._summer_start = datetime.strptime(
            data.get("summer_start"), "%Y-%m-%d"
        )
        self._summer_end = datetime.strptime(data.get("summer_end"), "%Y-%m-%d")
        self._summer_rate = data.get("summer_rate")
        self._regular_rate = data.get("regular_rate")
        self._regular_service_charge = data.get("regular_service_charge")

    @property
    def summer_start(self):
        return self._summer_start

    @property
    def summer_end(self):
        return self._summer_end

    @property
    def summer_rate(self):
        return self._summer_rate

    @property
    def regular_rate(self):
        return self._regular_rate

    @property
    def regular_service_charge(self):
        return self._regular_service_charge
