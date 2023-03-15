from django.urls import path

from . import views

urlpatterns = [
    path('', views.Proxy.as_view()),
    path('<int:id>', views.Proxy.as_view()),
]
