import json

from django.http import HttpResponse, JsonResponse
from example import dto, service
from rest_framework.views import APIView


class Proxy(APIView):

    def get(self, request, id=None):
        if id == None:
            return JsonResponse(service.list(), safe=False)

        example = service.get(id)
        if not example:
            return HttpResponse(status=204)
        return JsonResponse(dto.example_to_json(example))

    def post(self, request):
        body = json.loads(request.body.decode('utf-8'))
        id = service.save(dto.json_to_example(body))
        return JsonResponse({'id': id})

    def delete(self, request, id):
        service.delete(id)
        return HttpResponse(status=204)
