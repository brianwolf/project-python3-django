from django.urls import path

from . import views

urlpatterns = [
    path('', views.Root.as_view()),
    path('<int:id>', views.ById.as_view()),
]
