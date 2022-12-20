from django.urls import path
from . import views
# from django.conf.urls import url

# app_name = 'tests'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:kits_id>/', views.detail, name='detail'),
    path('answer/<int:kits_id>/<int:riddle_id>/', views.answer, name='answer'),
    # path('result/', views.result, name='result'),

]
