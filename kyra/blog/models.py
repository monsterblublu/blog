from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()

from django.utils.text import slugify
from django.utils import timezone
from django_summernote.fields import SummernoteTextField

# Create your models here.
class Article(models.Model):
    author = models.CharField(max_length=90)
    title = models.CharField(max_length=255)
    snippet = models.CharField(max_length=100,blank=True)
    thumbnail = models.ImageField(upload_to='article/thumbnail',blank=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    text = SummernoteTextField()
    created_at = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'slug':self.slug})
