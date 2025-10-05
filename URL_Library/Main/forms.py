from django import forms

class URLForm(forms.Form):
    url = forms.URLField(label='Enter a URL', max_length=200)