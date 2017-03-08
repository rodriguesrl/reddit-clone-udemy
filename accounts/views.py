from django.contrib.auth import authenticate, login, logout
from django.views.generic import RedirectView, CreateView
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy


################## CLASS BASED VIEWS #####################

class SignUpView(CreateView):
	model = User
	success_url = reverse_lazy('home')
	error_url = reverse_lazy('accounts:signup')
	template_name = 'accounts/signup.html'
	fields = ['username', 'password']
	def post(self, request, *args, **kwargs):
		if (request.POST['password1'] == request.POST['password2'] and request.POST['password1'] != ''):
			try:
				User.objects.get(username=request.POST['username'])
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
				login(request, user)
				return HttpResponseRedirect(self.success_url)
		return self.get(request, *args, **kwargs)

################## FUNCTION BASED VIEWS #####################
# def signup(request):
# 	if (request.method == "POST"):
# 		if request.POST['password1'] == request.POST['password2']:
# 			try:
# 				User.objects.get(username=request.POST['username'])
# 				return render(request, 'accounts/signup.html', {'error': 'Username already exists!'})
# 			except User.DoesNotExist:
# 				user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
# 				login(request, user)
# 				return redirect('home')
			
# 		else:
# 			return render(request, 'accounts/signup.html', {'error': 'Passwords mismatch!'})
# 	else:
# 		return render(request, 'accounts/signup.html')

# def signin(request):
# 	if (request.method == "POST"):
# 		if request.POST['username'] and request.POST['password']:
# 			username = request.POST['username']
# 			password = request.POST['password']
# 			user = authenticate(username=username, password=password)
# 			if (user is not None):
# 				login(request, user)

# 				if 'next' in request.POST:
# 					return redirect(request.POST['next'])

# 				return redirect('home')
# 			else:
# 				return render(request, 'accounts/signin.html', {'error': 'Wrong username or password!'})
			
# 		else:
# 			return render(request, 'accounts/signin.html', {'error': 'Empty Fields! Fill\'em'})
# 	else:
# 		return render(request, 'accounts/signin.html')

# def signout(request):
# 	logout(request)
# 	return redirect('home')