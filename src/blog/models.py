from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

# Create your models here.

class BlogPostQuerySet(models.QuerySet):
	def published(self):
		now = timezone.now()
		return self.filter(publish_date__lte=now)

class BlogPostManager(models.Manager):
	def get_queryset(self):
		return BlogPostQuerySet(self.model, using=self._db)

	def published(self):
		return self.get_queryset().published()


class BlogPost(models.Model):
	user = models.ForeignKey(User, default=1, on_delete=models.SET_NULL, null = True)
	slug = models.SlugField(unique=True)
	title = models.CharField(max_length=120)
	content = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to='image/',blank=True, null=True)
	publish_date = models.DateTimeField(auto_now=False,auto_now_add=False,null=True,blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	objects = BlogPostManager()

	class Meta:
		ordering=['-publish_date','-updated','-timestamp']

	def get_absolute_url(self):
		return f"/blog/{self.slug}"

	def get_edit_url(self):
		return f"/blog/{self.slug}/edit"

	def get_delete_url(self):
		return f"/blog/{self.slug}/delete/"


