from django import forms
from webadmin.core.models import *

class ProjForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProjForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = Proj


class IPForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(IPForm, self).__init__(*args, **kwargs)

    class Meta:
        model = IP

class HostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(HostForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Host

class IDCForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(IDCForm, self).__init__(*args, **kwargs)

    class Meta:
        model = IDC

class CForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField()
