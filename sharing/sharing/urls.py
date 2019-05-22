from django.contrib import admin
from django.urls import path, include
from main import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.main_page, name='main_page')
    path('', include('main.urls')),
    path('', include('files_sharing.urls')),
]

