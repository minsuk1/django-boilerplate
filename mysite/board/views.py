from django.views import View
from django.http import JsonResponse


class first(View):
    def get(self, request):
        return JsonResponse("hello world", safe=False)

    def post(self, request):
        print(request.data)
        return JsonResponse(request.data, safe=False)