from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('stamps/', views.stamps_index, name='index'),
    path('stamps/<int:stamp_id>/', views.stamp_details, name='detail'),
    path('stamps/create', views.StampCreate.as_view(), name='stamps_create'),
    path('stamps/<int:pk>/update', views.StampUpdate.as_view(), name='stamps_update'),
    path('stamps/<int:pk>/delete', views.StampDelete.as_view(), name='stamps_delete'),
]