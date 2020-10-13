import random
import string
from django.conf import settings

SHORTCODE_MIN = getattr(settings,"SHORTCODE_MIN",6)

def code_generator(length, chars= string.ascii_lowercase + string.digits):
    return ''.join(random.choices(chars,k=length))

def create_shortcode(instance,length=SHORTCODE_MIN):
    new_shortcode = code_generator(length)
    # print(instance)
    # print(instance.__class__)
    # print(instance.__class__.__name__)
    ShortenURLClass = instance.__class__
    sc_exists = ShortenURLClass.objects.filter(shortcode=new_shortcode).exists()

    if sc_exists:
        return create_shortcode(length)
    return new_shortcode
 
