from django.conf.urls import url
from . import views

app_name = "posts"

urlpatterns = [
    #Class Based Views URLs
    url(r'^(?P<pk>[0-9]+)/downvote', views.DownvoteView.as_view(), name="downvote"),
    url(r'^(?P<pk>[0-9]+)/upvote', views.UpvoteView.as_view(), name="upvote"),
    url(r'^user/(?P<pk>[0-9]+)', views.ByUserView.as_view(), name="byuser"),
    url(r'^create/', views.CreatePostView.as_view(), name="create"),
    
    #Function Based Views URLs
    #url(r'^create/', views.create, name="create"),
    #url(r'^(?P<pk>[0-9]+)/upvote', views.upvote, name="upvote"),
    #url(r'^(?P<pk>[0-9]+)/downvote', views.downvote, name="downvote"),
    #url(r'^user/(?P<userid>[0-9]+)', views.byuser, name="byuser"),

]
