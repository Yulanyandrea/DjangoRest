from django.contrib import admin
from django.urls import path
from api.views.hello import helloworld

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',helloworld)
]
