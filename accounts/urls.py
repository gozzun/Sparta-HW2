from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("profile/<str:username>/", views.profile, name="profile"),
    path("<int:user_id>/follow/", views.follow, name="follow"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("update/", views.update, name="update"),
    path("password/", views.change_password, name="change_password"),
    path("delete/", views.delete, name="delete"),
    path("update-image/", views.update_image, name="update_image"),
    path("delete-image/", views.delete_image, name="delete_image"),
]