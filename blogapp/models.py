from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    
    class Status(models.TextChoices):
        DRAFT = 'DR', 'Draft',
        PUBLISHED = 'PB', 'Published'
    
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    publish = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices = Status.choices, default=Status.DRAFT)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, related_name="author_blog")
    likes = models.ManyToManyField(User)
    category = models.ManyToManyField("Category")

    # class Meta:
    #     ordering = ['-publish']

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})  
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    body = models.TextField()
    user = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add = True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    
    def __str__(self):
        return self.body

class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
    