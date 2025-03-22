from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/signup/', AdminSignupView.as_view(), name='admin-signup'),  # Admin Signup
    path("admin/login/", TokenObtainPairView.as_view(), name="admin-login"),  # Admin Login
    path("admin/refresh/", TokenRefreshView.as_view(), name="token-refresh"),  # Refresh Token
    path("book/", BookView.as_view(), name="book-list"),  # GET (list all), POST (create)
    path("book/<int:pk>/", BookView.as_view(), name="book-detail"),  # GET (retrieve), PUT (update), DELETE (delete)
]