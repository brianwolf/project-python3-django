import logging

from decouple import config
from django.http import JsonResponse

logger = logging.getLogger(__name__)


def index(request):

    VERSION = config("VERSION", cast=str)

    logger.info(f'Version: {VERSION}')
    return JsonResponse({'version': VERSION})
