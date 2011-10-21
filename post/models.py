from django.db import models
import datetime

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    pub_date=models.DateTimeField()
    categories=models.ManyToManyField(Category)

    def __unicode__(self):
        return self.title
