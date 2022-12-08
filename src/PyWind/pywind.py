import json
from src.PyWind.services.smhi import SmhiGateway


class PyWind:
    @staticmethod
    def get_bjorko_farjan_wind_collection() -> None:
        winds = SmhiGateway.get_bjorko_farjan_wind_forecasts()
        json_winds = [json.dumps(x.__dict__) for x in winds]
        print(",\n".join(json_winds))


PyWind.get_bjorko_farjan_wind_collection()