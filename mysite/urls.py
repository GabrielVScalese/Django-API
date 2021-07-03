from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def index(request):
    return HttpResponse('API is running!')

urlpatterns = [
    path('', index), 
    path('api/', include('polls.api.urls')),
    path('admin/', admin.site.urls),
]
