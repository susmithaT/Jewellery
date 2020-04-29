

from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_view
from django.views.generic.base import TemplateView
urlpatterns = [

    #path('account/login',auth_view.LoginView.as_view(),name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('main/',TemplateView.as_view(template_name='home.html'),name='home'),

    #path('login/', views.login_user),

]

