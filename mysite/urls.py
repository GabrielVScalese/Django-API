from django.contrib import admin
from django.urls import path, include
from django.http.response import JsonResponse

def index(request):
    return JsonResponse({'message': 'API is running!'})

urlpatterns = [
    path('', index), 
    path('api/', include('polls.api.urls')),
    path('admin/', admin.site.urls),
]
