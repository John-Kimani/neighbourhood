from django import forms
from .models import Neighborhood


class HoodRegistrationForm(forms.ModelForm):
    '''
    Hood registration form
    '''
    class Meta:
        model = Neighborhood
        fields = '__all__'