from django import forms

my_default_errors = {
    'required': 'This field is required',
    'invalid': 'Invalid URL. Please enter a valid url'
}
class SubmitURLForm(forms.Form):
    url = forms.URLField(label='',
            widget=forms.URLInput(attrs={'placeholder': 'Paste long URL to shorten e.g. http:\\\\google.com'})
                                        , error_messages = my_default_errors)
