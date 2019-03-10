from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
    #to złapie pathy typu .../blog/3
    #w views dodamy funkcję def detail(request, blog_id): i użyjemy blog_id
]