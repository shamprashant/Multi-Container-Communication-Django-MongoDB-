from django.urls import path, re_path
from django.urls.resolvers import URLPattern
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.index, name = 'index_page'),
    path('form/', views.print_both, name = 'print_both'),
    re_path('feedback/[a-zA-Z]+', views.show_file_data, name = 'show_file_data')
]