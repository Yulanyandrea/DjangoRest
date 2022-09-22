from django.contrib import admin
from django.urls import path
from api import views
from api.views import taskView
from api.views.hello import helloworld
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from api.views.userCreateView import UserCreateView
from api.views.userDetailView import UserDetailView
from rest_framework.routers import DefaultRouter
from api.views.taskView import TaskView

router=DefaultRouter()
router.register(r'task',TaskView, basename='task')


urlpatterns = [
    
    
    path('login/',TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('user/',UserCreateView.as_view()),
    path('user/<int:pk>/',UserDetailView.as_view()), #pk primary key
   # path('task/',TaskView.as_view())
]

urlpatterns+=router.urls