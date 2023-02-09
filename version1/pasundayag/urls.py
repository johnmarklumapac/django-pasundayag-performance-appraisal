from django.urls import path

from . import views

app_name = 'pasundayag'

urlpatterns = [
    path('', views.ipcr_all, name='pasundayag_home'),
    path('<slug:slug>', views.ipcr_detail, name='ipcr_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
]
