from django.urls import path

# import my_view from todo Application
from .views import index, create_view, update_view, delete_view

app_name = 'gizibayi'
urlpatterns = [
    path('', index, name='home'),
    
    # url untuk halaman tambah task
    path('create', create_view, name='create'),
    
    # url untuk halaman ubah task
    path('update/<int:bayi_id>', update_view, name='update'),
    
    # url untuk menghapus task
    path('delete/<int:bayi_id>', delete_view, name='delete'),
]