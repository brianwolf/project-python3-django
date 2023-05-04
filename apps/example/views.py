import json

from django.http import HttpResponse, JsonResponse
from example import dto, service
from rest_framework.views import APIView


class Root(APIView):

    def get(self, _):
        return JsonResponse(service.list(), safe=False)

    def post(self, request):
        body = json.loads(request.body)
        _id = service.save(dto.json_to_example(body))
        return JsonResponse({'id': _id}, status=201)


class ById(APIView):

    def get(self, _, id):
        example = service.get(id)
        if not example:
            return HttpResponse(status=204)
        return JsonResponse(dto.example_to_json(example))

    def delete(self, _, id):
        service.delete(id)
        return HttpResponse(status=204)
