from django.db import models
from .utils import create_shortcode
from django.conf import settings
from django.urls import reverse
# Create your models here.

SHORTCODE_MAX = getattr(settings,"SHORTCODE_MAX",15)
URL_START_STRING = getattr(settings,"URL_START_STRING")

# You can make a model manager for this ShortenURL model like this:
class ShortenURLManager(models.Manager):
    # You can override the manger methods e.g all or even make your own manager methods
    def refresh_shortcodes(self):
        qs = ShortenURL.objects.filter(id__gte=1)
        new_codes_made = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_codes_made +=1
        return "New codes made {}".format(new_codes_made)


class ShortenURL(models.Model):
    url = models.URLField(max_length = 220, )
    shortcode = models.SlugField(max_length = SHORTCODE_MAX,unique = True, blank=True)
    updated = models.DateTimeField(auto_now = True)
    timestamp = models.DateTimeField(auto_now_add =True)
# Attach the ShortenURLManager to the objects
    objects = ShortenURLManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(ShortenURL,self).save(*args,**kwargs)

    def __str__(self):
        return str(self.url)

    def get_short_url(self):
        url_path = reverse('shortenurl',kwargs={'shortcode':self.shortcode})
        return URL_START_STRING+url_path
