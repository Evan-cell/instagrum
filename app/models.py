from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.urls import reverse

def user_directory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id,filename)
class Tag(models.Model):
    title = models.CharField(max_length=75, verbose_name='Tag')
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        verbose_name_prural = 'Tags'

        def get_absolute_url(self):
            return reverse('tags', args=[self.slug])
        def __str__(self):
            self.title 
        def save(self, *args, **kwargs):
            if not self.slug:
                self.slug = slugify(self.title)  
            return super().save(*args, **kwargs)         
            
