from django.urls import path, include
from . import views

urlpatterns = [
    path('test',views.test),
    path('test1',views.test1),
    path('test2',views.test2),
    path('test3',views.test3),
]