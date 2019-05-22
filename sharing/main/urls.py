from django.urls import path
from main import views


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('logout/', views.logout_view, name='logout'),
]
