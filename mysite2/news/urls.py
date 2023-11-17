from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('all/',views.all, name='all'),
    path('trending/',views.trending, name='trending'),
    path('sports/',views.sports, name='sports'),
    path('politics/',views.politics, name='politics'),
    path('lifeStyle/',views.lifeStyle, name='lifeStlye'),
    path('healty/',views.healty, name='healty'),
    path('entertaiment/',views.entertaiment, name='entertaiment'),
    path('isi/<int:id>',views.isi, name='isi')
]

