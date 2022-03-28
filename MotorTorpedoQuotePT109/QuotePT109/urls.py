from django.urls import path
from QuotePT109 import views

app_name = 'QuotePT109'
urlpatterns = [
    path('', views.index, name='index'),
    path('generator/', views.preGenerator, name='generator'),
    path('login/', views.login, name='login'),
    path('generator/comedic/', views.comedicGenerated, name='generatedComedic'),
    path('generator/inspirational/', views.inspirationalGenerated, name='generatedInspiring'),
    path('generator/philisophical/', views.philisophicalGenerated, name='generatedPhilisophical'),
]