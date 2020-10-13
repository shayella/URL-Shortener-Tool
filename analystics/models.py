from django.db import models
from shortener.models import ShortenURL
# Create your models here.

class ClickEventManager(models.Manager):
    def create_event(self,instance):
        if isinstance(instance,ShortenURL):
            obj,created = self.get_or_create(short_url=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    short_url = models.OneToOneField(ShortenURL,on_delete=models.CASCADE,)
    count = models.IntegerField(default = 0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return str(self.short_url)
