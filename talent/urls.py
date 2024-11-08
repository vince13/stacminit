from django.urls import path
from . import views

app_name = "talent"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),

    # Authentication
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),


    # Students Registration
    path("new-student/", views.new_student, name="new-student"),

]

