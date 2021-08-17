from django.urls import path,include

from accounts import views



urlpatterns = [
    path('login_view/', views.login_view, name = 'login_view'),
    path('register/', views.register, name = 'register'),
    
    path('logout_view/', views.logout_view, name = 'logout'),
    path('admin_dashboard/', views.admin_dashboard, name = 'admin_dashboard'),
    path('admin_login/', views.admin_login, name = 'admin_login'),
    path('admin_logout/', views.admin_logout, name = 'admin_logout'),
    path('validate_username/', views.validate_username, name = 'validate_username'),
    path('validate_email/', views.validate_email, name = 'validate_email'),
    path('verify_otp/', views.verify_otp, name = 'verify_otp'),
    path('otp_login/', views.otp_login, name = 'otp_login'),

    ]