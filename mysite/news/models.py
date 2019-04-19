from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    class Meta:
        verbose_name_plural='Categories'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class News(models.Model):
    class Meta:
        verbose_name_plural='News'
    author=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=200)
    image = models.ImageField( blank=True, null=True)
    context = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title




# Create your models here.
