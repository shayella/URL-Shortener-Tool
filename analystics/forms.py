from django import forms
from django.core.exceptions import ValidationError

class URLCountForm(forms.Form):
    short_url = forms.URLField(label='Short URL',
            widget=forms.URLInput(attrs={'placeholder': 'Enter your short URL'}))

    
