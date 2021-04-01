from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    owner       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category    = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    title       = models.CharField(max_length=100, blank=False, null=False)
    slug        = models.SlugField(max_length=100, unique=True, allow_unicode=True)
    text        = models.TextField()
    image       = models.ImageField(upload_to='post-images')
    create_date = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('blog:post-detail', args=[self.slug])

    class Meta:
        ordering = ('-create_date', )

    def __str__(self):
        return self.title


class Entry(models.Model):
    post            = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='entries')
    headline        = models.CharField(max_length=255, blank=True)
    text            = models.TextField()
    image           = models.ImageField(upload_to='entries-images', blank=True, null=True)
    create_date     = models.DateField(auto_now_add=True)
    update_time     = models.DateField(auto_now=True)

    class Meta:
        ordering = ('create_date', )

    def __str__(self):
        return self.headline


class Comments(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post        = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text        = models.TextField()
    active      = models.BooleanField(default=True)
    create_date = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True)

    class Meta:
        ordering = ('-create_date', )

    def __str__(self):
        return self.post.title
