from __future__ import unicode_literals

import django.urls
from django.contrib.auth.urls import path
import django.contrib.auth.views

from accountsplus import views
from accountsplus import forms

urlpatterns = [
    path('logout/', views.logout_then_login, name='logout'),
    path('password_change/', views.password_change, name='password_change'),
    path('password_reset/', views.password_reset, name='password_reset'),
    django.urls.re_path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        django.contrib.auth.views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    # override the admin password reset flow to use the normal site password
    # reset flow
    path('password_reset/', views.password_reset, name='admin_password_reset'),

    path('login/',
        django.contrib.auth.views.LoginView.as_view(),
        kwargs={'authentication_form': forms.EmailBasedAuthenticationForm, 'redirect_authenticated_user': True},
        name='login'),
    path('', django.conf.urls.include(django.contrib.auth.urls)),

    # masquerade views
    path('admin/masquerade/end/', views.end_masquerade, name='end_masquerade'),
    path('admin/masquerade/<int:user_id>/', views.masquerade, name='masquerade'),
]
