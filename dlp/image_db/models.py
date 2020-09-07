from django.db import models
from django.db.models.aggregates import Count
from random import randint

# Create your models here.
class Keyword(models.Model):
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value

class KeywordSet(models.Model):
    keywords = models.ManyToManyField(Keyword)

    def __str__(self):
        return ''.join([keyword.value + ", " for keyword in self.keywords.all()[:10]])

class ImageType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ImageEntry(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img/')
    image_type = models.ForeignKey(ImageType, null=True, blank=True, on_delete=models.SET_NULL)
    keywords_set = models.ManyToManyField(KeywordSet, blank=True)

    @classmethod
    def random_id(cls):
        count = cls.objects.aggregate(count=Count('id'))['count'] # todo: modify for selecting associated with image type or list of image types
        return cls.objects.all()[randint(0, count - 1)].id
    def __str__(self):
        return self.name