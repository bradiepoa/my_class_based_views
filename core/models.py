from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Core(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='core')
    slug = models.SlugField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('core:single', args=[self.slug])
    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.title


# Create your models here.
