from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from .helpers import generate_slug



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)

class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = RichTextField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    user = models.ForeignKey(User, blank=True, null=True,
                             on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    genre = models.TextField(max_length=10, null=True)
  
    def __str__(self):
      return self.title


    def save(self, *args, **kwargs):
      self.slug = generate_slug(self.title)
      super(BlogModel, self).save(*args, **kwargs)

class Subscribers(models.Model):
      username = models.CharField(max_length=100)
      email = models.EmailField(max_length=254)
      email_token = models.CharField(max_length=100)
      is_verified = models.BooleanField(default=False)

      def __str__(self):
            return self.username

