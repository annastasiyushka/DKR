from django.conf.urls import url
from . import views

urlpatterns = [
    url('registration', views.ClientRegister.as_view()),
    url('login', views.ClientLogin.as_view()),
    url('logout', views.ClientLogout.as_view())
]