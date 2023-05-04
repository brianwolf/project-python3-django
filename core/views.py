import logging

from decouple import config
from django.http import JsonResponse
from rest_framework.views import APIView

logger = logging.getLogger(__name__)


class Root(APIView):

    def get(self, _):
        VERSION = config("VERSION", cast=str)
        logger.info(f'Version: {VERSION}')
        return JsonResponse({'version': VERSION})
