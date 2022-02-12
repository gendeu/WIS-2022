from django.urls import path, include
from frontend import views

urlpatterns = [
    path("", views.render_login, name="render_login"),
    path('api/', include('api.urls')),
    
    path("signup", views.render_signup, name="render_signup"),
    path("login", views.perform_login, name="perform_login"),
    path("home", views.render_home, name="render_home"),
    path("logout", views.perform_logout, name="perform_logout"),
    path("register", views.perform_register, name='perform_register'),
    path("users", views.show_users, name='show_users'),
    # path("success", views.render_success, name='render_success'),
]