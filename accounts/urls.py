from django.conf.urls import url
from . import views

app_name = "accounts"

urlpatterns = [
    url(r'^signup/', views.signup, name="signup"),
    url(r'^signin/', views.signin, name="signin"),
    url(r'^logout/', views.signout, name="logout"),
]
