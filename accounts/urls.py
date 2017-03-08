from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

app_name = "accounts"

urlpatterns = [
	#Class Based Views URLs
	url(r'^login/$', auth_views.login, {'template_name': 'accounts/signin.html'}, name='signin'),
	url(r'^signup/', views.SignUpView.as_view(), name="signup"),
	url(r'^logout/', auth_views.logout, name="logout"),
	
	#Function Based Views URLs
    #url(r'^signup/', views.signup, name="signup"),
    #url(r'^signin/', views.signin, name="signin"),
    #url(r'^logout/', views.signout, name="logout"),
]
