from django.urls import path
from files_sharing import views


urlpatterns = [
    path('upload/', views.file_upload_page, name='index_page'),
    path('file-upload/', views.save_file, name='file_upload_ajax'),
    path('user-files/', views.user_files_page, name='uploaded_files_by_user'),
]
