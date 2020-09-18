from django.urls import path
from blog import views

urlpatterns = [
    path("", views.index, name="home"),
    path("login", views.loginUser, name="login"),
    # path("logout", views.logoutUser, name="logout"),
    # path("contact", views.contact, name="contact"),
    # path("about", views.about, name="about")
]