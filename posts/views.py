from django.views.generic import RedirectView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import ProcessFormView
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from .forms import NewPostForm
from django import forms
from . import models


################## CLASS BASED VIEWS #####################
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
		return super().get_queryset().filter(author = self.kwargs.get('pk')).order_by('-votes')


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


################## FUNCTION BASED VIEWS #####################
# @login_required(login_url='/accounts/signin/')
# def create(request):
# 	if request.method == "POST":
# 		if request.POST['title'] and request.POST['url']:
# 			post = models.Post()
# 			post.title = request.POST['title']
# 			if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
# 				post.url = request.POST['url']
# 			else:
# 				post.url = 'http://' + request.POST['url']
# 			post.date = timezone.datetime.now()
# 			post.author = request.user
# 			post.save()
# 			return redirect('home')
# 		else:
# 			return render(request, 'posts/create.html', {'message': 'Preencha os campos!'})
# 	else:
# 		return render(request, 'posts/create.html')

# def home(request):
# 	posts = models.Post.objects.order_by('-votes')
# 	return render(request, 'posts/home.html', {'posts': posts})

# def upvote(request, pk):
# 	if request.method == "POST":
# 		post = models.Post.objects.get(pk=pk)
# 		post.votes += 1
# 		post.save()
# 		if request.POST['from'] == 'home':
# 			return redirect('home')
# 		else:
# 			return redirect('posts:byuser', userid=post.author.id)

# def downvote(request, pk):
# 	if request.method == "POST":
# 		post = models.Post.objects.get(pk=pk)
# 		post.votes -= 1
# 		post.save()
# 		#Redirect to the correct page
# 		if request.POST['from'] == 'home':
# 			return redirect('home')
# 		else:
# 			return redirect('posts:byuser', userid=post.author.id)

# def byuser(request, pk):
# 	posts = models.Post.objects.filter(author=pk).order_by('-votes')
# 	return render(request, 'posts/byuser.html', {'posts': posts})
