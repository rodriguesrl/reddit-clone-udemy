from django.views.generic import RedirectView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.utils import timezone
from .forms import NewPostForm
from . import models


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('accounts:signin')
    template_name = 'posts/create.html'
    form_class = NewPostForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.date = timezone.datetime.now()
        return super().form_valid(form)


class HomeView(ListView):
    template_name = "posts/home.html"
    queryset = models.Post.objects.order_by('-votes')


class ByUserView(ListView):
    template_name = "posts/byuser.html"
    model = models.Post

    def get_queryset(self, **kwargs):
        return super().get_queryset().filter(author=self.kwargs.get('pk')).order_by('-votes')


class UpvoteView(RedirectView):
    def post(self, request, *args, **kwargs):
        post = models.Post.objects.get(pk=self.kwargs.get('pk'))
        post.votes += 1
        post.save()

        if (self.request.POST['from'] == 'home'):
            self.url = reverse_lazy('home')
        elif (self.request.POST['from'] == 'user'):
            self.url = reverse_lazy('posts:byuser', args=[str(post.author.id)])

        return self.get(request, *args, **kwargs)


class DownvoteView(RedirectView):
    def post(self, request, *args, **kwargs):
        post = models.Post.objects.get(pk=self.kwargs.get('pk'))
        post.votes -= 1
        post.save()

        if (self.request.POST['from'] == 'home'):
            self.url = reverse_lazy('home')
        elif (self.request.POST['from'] == 'user'):
            self.url = reverse_lazy('posts:byuser', args=[str(post.author.id)])

        return self.get(request, *args, **kwargs)
