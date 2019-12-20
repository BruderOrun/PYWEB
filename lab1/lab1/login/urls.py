from django.urls import path
from lab1.login.views import LoginView

urlpatterns = [
    path('', LoginView.as_view()),
]