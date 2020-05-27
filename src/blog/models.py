from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.

class BlogPost(models.Model):
	user = models.ForeignKey(User, default=1, on_delete=models.SET_NULL, null = True)
	slug = models.SlugField(unique=True)
	title = models.CharField(max_length=120)
	content = models.TextField(null=True, blank=True)