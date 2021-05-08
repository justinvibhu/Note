from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path('home/<username>/',views.home,name='home'),
    path('add_task',views.add_task,name='add'),
    path('delete',views.delete,name='delete'),
]