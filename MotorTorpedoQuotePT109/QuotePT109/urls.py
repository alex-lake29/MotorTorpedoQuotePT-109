from django.urls import path
from QuotePT109 import views

app_name = 'QuotePT109'
urlpatterns = [
    path('', views.index, name='index'),
    path('generator/', views.preGenerator, name='generator'),
    path('login/', views.login, name='login'),
    path('generator/comedic/', views.generatorC, name='generatorC'),
    path('generator/generated/', views.generated, name='generated'),
]