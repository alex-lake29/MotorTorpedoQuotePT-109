from django.urls import path
from QuotePT109 import views

app_name = 'QuotePT109'
urlpatterns = [
path('', views.index, name='index'),
]