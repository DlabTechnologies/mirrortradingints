from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('withdraw_not_eligable/', views.withdraw_not_eligable, name='withdraw_not_eligable'),
    path('withdraw_complete_error/', views.withdraw_complete_error, name='withdraw_complete_error'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('deposit/', views.deposit, name='deposit'),
    path('deposit_complete/', views.deposit_complete, name='deposit_complete'),
    path('personal_info/', views.personal_info, name='personal_info'),
    path('transaction_history/', views.transaction_history, name='transaction_history'),
    path('account_types', views.account_types, name='account_types'),
    path('register', views.Signup_view, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('login', views.login_view, name='login'),
    path('personal_info', views.personal_info, name='personal_info'),
    path('validate_otp', views.validate_phone_otp, name='validate_otp'),
    path('send_otp', views.send_otp, name='send_otp'),
    path('account_upgrade', views.send_upgrade_email, name='account_upgrade'),
    path('change_email_address', views.change_email_address, name='change_email_address'),


     # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='account/password_change.html'), 
        name='password_change'),
    
    #password reset 
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset.html'), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset_form.html'), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
     name='password_reset_complete'),
]


urlpatterns += staticfiles_urlpatterns()