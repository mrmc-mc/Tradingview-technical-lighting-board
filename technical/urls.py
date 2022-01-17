from django.urls import path,include
from . import views


app="technical"
urlpatterns = [
    path('', views.Index.as_view(),name="tindex"),
]