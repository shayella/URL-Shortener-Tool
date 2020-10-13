from django.core.management.base import BaseCommand,CommandError
from shortener.models import ShortenURL

class Command(BaseCommand):
    help = 'Refreshes all shortcodes for the ShortenURL objects'

    def handle(self,*args,**options):
        return ShortenURL.objects.refresh_shortcodes()
