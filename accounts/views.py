from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.urls import reverse_lazy


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
