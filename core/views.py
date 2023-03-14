from decouple import config
from django.http import JsonResponse


def index(request):
    VERSION = config("VERSION", cast=str)
    return JsonResponse({'version': VERSION})
