from django.views import View
from django.http import JsonResponse
from django.core.cache import cache
from .models import Post




class first(View):
    def get(self, request):
        return JsonResponse("hello world", safe=False)

    def post(self, request):
        print(request.data)
        return JsonResponse(request.data, safe=False)



import json
class redis(View):
    def get(self, request):
        posts = cache.get_or_set('posts', Post.objects.all().values('id', 'text'))
        return JsonResponse(list(posts), safe=False)

    def post(self, request):
        print(json.loads(request.body))
        data = json.loads(request.body)
        data = data['text']
        b = Post(text=data)
        b.save()
        return JsonResponse("ok", safe=False)