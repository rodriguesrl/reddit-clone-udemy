from django.conf.urls import url, include
from django.contrib import admin
from posts import views

urlpatterns = [
	#Function Based Views URLs
    #url(r'^$', views.home, name="home"),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^posts/', include('posts.urls')),

    #Class Based Views URLs
    url(r'^$', views.HomeView.as_view(), name="home")
]
