from django.urls import path
from .views import Register,Login,Logaut,AllUser,Change

urlpatterns = [
    path("AllUser/",AllUser.as_view()),
    path("register/",Register.as_view()),
    path("Login/",Login.as_view()),
    path("Logaut/<str:name>/",Logaut.as_view()),
    path("Change/",Change.as_view()),
]