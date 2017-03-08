from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=200)
	url = models.URLField()
	date = models.DateTimeField()
	author = models.ForeignKey(User)
	votes = models.IntegerField(default=1)

	def __str__(self):
		return self.title

	def date_pretty(self):
		return self.date.strftime('%b %e %Y')