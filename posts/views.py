from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from . import models


@login_required(login_url='/accounts/signin/')
def create(request):
	if request.method == "POST":
		if request.POST['title'] and request.POST['url']:
			post = models.Post()
			post.title = request.POST['title']
			if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
				post.url = request.POST['url']
			else:
				post.url = 'http://' + request.POST['url']
			post.date = timezone.datetime.now()
			post.author = request.user
			post.save()
			return redirect('home')
		else:
			return render(request, 'posts/create.html', {'message': 'Preencha os campos!'})
	else:
		return render(request, 'posts/create.html')

def home(request):
	posts = models.Post.objects.order_by('-votes')
	return render(request, 'posts/home.html', {'posts': posts})

def upvote(request, pk):
	if request.method == "POST":
		post = models.Post.objects.get(pk=pk)
		post.votes += 1
		post.save()
		if request.POST['from'] == 'home':
			return redirect('home')
		else:
			return redirect('posts:byuser', userid=post.author.id)

def downvote(request, pk):
	if request.method == "POST":
		post = models.Post.objects.get(pk=pk)
		post.votes -= 1
		post.save()
		#Redirect to the correct page
		if request.POST['from'] == 'home':
			return redirect('home')
		else:
			return redirect('posts:byuser', userid=post.author.id)

def byuser(request, userid):
	posts = models.Post.objects.filter(author=userid).order_by('-votes')
	return render(request, 'posts/byuser.html', {'posts': posts})