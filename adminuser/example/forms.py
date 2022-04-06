from django import forms
from .models import Person
from django.contrib.auth import authenticate,get_user_model
from django.contrib.auth.forms import PasswordChangeForm

class usrForm(forms.ModelForm):
    password = forms.CharField(initial=123)
    
    class Meta:
        model = Person
        fields = ('first_name','last_name','username','email','password','position')


    def __init__(self, *args, **kwargs):
        super(usrForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label = "Select"

class usrChange(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('username','password')
        widgets= {
            'password' : forms.PasswordInput(),
            }

class loginForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('username','password')
        widgets= {
            'password' : forms.PasswordInput(),
            }
    
    

