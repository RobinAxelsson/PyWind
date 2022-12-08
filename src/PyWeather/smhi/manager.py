from . import SmhiPointRequest
from .repository import get_json_point_request
from .parser import parse_point_request


def get_point_request() -> SmhiPointRequest:
    json_request = get_json_point_request()
    return parse_point_request(json_request)