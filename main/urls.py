from django.urls import path
from main import views


urlpatterns=[
    path('',views.index,name='index'),
    path('article/<int:pk>/',views.get_article,name='get_article'),
    path('author/<int:pk>/',views.get_author,name='get_author'),
    path('create/',views.create_article,name='create_article'),
]