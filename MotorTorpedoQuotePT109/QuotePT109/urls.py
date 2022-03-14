from django.urls import path
from QuotePT109 import views

app_name = 'QuotePT109'
urlpatterns = [
    path('', views.index, name='index'),
    path('generator/', views.generator, name='generator'),
    path('login/', views.login, name='login'),
    path('about/', views.login, name='about'),
    path('generator/generated/', views.login, name='generated'),
]