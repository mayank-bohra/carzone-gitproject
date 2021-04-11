
from django.urls import path
from .import views
urlpatterns = [
    paths('',views.home,name='home'),
]
