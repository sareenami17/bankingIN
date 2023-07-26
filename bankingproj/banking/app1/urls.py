from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register',views.SignUpView.as_view(),name='register'),
    path('login',views.LoginView.as_view(),name="login"),
    path('logout',views.SignOutView.as_view(),name='logout'),
    path('account_form/', views.cascading_dropdown, name='account_form'),
    path('get_branches/<int:district_id>/', views.get_branches, name='get_branches'),
   # path('application',views.application_view,name='application')
   # path('account', views.account_form_view, name='account_form'),
    path('success/', views.success_page_view, name='success_page'),
]
