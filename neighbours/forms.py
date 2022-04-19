from django import forms
from .models import Neighborhood, Business, Hood


class HoodRegistrationForm(forms.ModelForm):
    '''
    Hood registration form
    '''
    class Meta:
        model = Hood
        fields = '__all__'


class  BusinessRegistrationForm(forms.ModelForm):
    '''
    Business registration form
    '''
    class Meta:
        model = Business
        fields = '__all__'