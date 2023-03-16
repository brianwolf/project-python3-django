import logging
from dataclasses import dataclass
from enum import Enum
from typing import Dict

from django.http import HttpResponse, JsonResponse

logger = logging.getLogger(__name__)


@dataclass
class AppException(Exception):
    code: Enum
    msj: str = None
    exception: Exception = None

    def to_json(self) -> Dict[str, object]:
        d = {'code': self.code.value, 'msj': self.msj}
        if self.exception:
            d['exception'] = str(self.exception)
        return d


class ErrorHandlerMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):

        if type(exception) == AppException:

            if exception.exception:
                logger.exception(exception.exception)

            logger.warning(f'{exception.code} -> {exception.msj}')
            return JsonResponse(exception.to_json(), status=409)

        logger.exception(exception)
        return HttpResponse("Error processing the request.", status=500)
