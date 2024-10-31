from django.urls import path
from .views import MaxsulotListAPI, MaxsulotDetail, KirimListAPI, ChiqimListAPI

urlpatterns = [
    path('maxsulotList/', MaxsulotListAPI.as_view()),
    path('maxsulotDetail/<int:pk>/', MaxsulotDetail.as_view()),
    path('KirimList/', KirimListAPI.as_view()),
    path('chiqim/', ChiqimListAPI.as_view())
]