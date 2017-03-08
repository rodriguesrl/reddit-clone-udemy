from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

app_name = "accounts"

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'accounts/signin.html'}, name='signin'),
    url(r'^signup/', views.SignUpView.as_view(), name="signup"),
    url(r'^logout/', auth_views.logout, name="logout"),
]
