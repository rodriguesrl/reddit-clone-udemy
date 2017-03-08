from django import forms
from . import models

class NewPostForm(forms.ModelForm):
	class Meta:
		model = models.Post
		fields = ('title', 'url')
			