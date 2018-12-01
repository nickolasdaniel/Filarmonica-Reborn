from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    # PasswordResetView,
    # PasswordResetDoneView,
    # PasswordResetConfirmView
    )
from . import views

urlpatterns= [
    path('', views.home),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    # path('reset_password/', PasswordResetView.as_view(), name="reset_password"),
    # path('reset_password/done/', PasswordResetDoneView.as_view(), name="reset_password_done"),
    # path('reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/)',
    #     PasswordResetConfirmView.as_view(), name="reset_password_confirm"),
]
