from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={''
                            'class':'bg-gray-200 pl-12 py-2 md:py-4 focus:outline-none w-full',
                            'type':'text',
                            'placeholder':'username',
                            'id': 'username' }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'type' : "password",
        'id' : "password",

    'class' : "bg-gray-200 pl-12 py-2 md:py-4 focus:outline-none w-full" ,
    'placeholder': 'Password'
    }))
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={''
                                                             'class': 'bg-gray-200 pl-12 py-2 md:py-4 focus:outline-none w-full',
                                                             'type': 'text',
                                                             'placeholder': 'First Name',
                                                             'id': 'username'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={''
                                                             'class': 'bg-gray-200 pl-12 py-2 md:py-4 focus:outline-none w-full',
                                                             'type': 'text',
                                                             'placeholder': 'Last Name',
                                                             'id': 'username'}))
    username = forms.CharField(widget=forms.TextInput(attrs={''
                                                             'class': 'bg-gray-200 pl-12 py-2 md:py-4 focus:outline-none w-full',
                                                             'type': 'text',
                                                             'placeholder': 'username',
                                                             'id': 'username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={''
                                                             'class': 'bg-gray-200 pl-12 py-2 md:py-4 focus:outline-none w-full',
                                                             'type': 'text',
                                                             'placeholder': 'email',
                                                             'id': 'username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={''
                                                             'class': 'bg-gray-200 pl-12 py-2 md:py-4 focus:outline-none w-full',
                                                             'type': 'text',
                                                             'placeholder': 'password',
                                                             'id': 'username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={''
                                                                  'class': 'bg-gray-200 pl-12 py-2 md:py-4 focus:outline-none w-full',
                                                                  'type': 'text',
                                                                  'placeholder': 'password',
                                                                  'id': 'username'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={''
                                                                  'class': 'bg-gray-200 pl-12 py-2 md:py-4 focus:outline-none w-full',
                                                                  'type': 'text',
                                                                  'placeholder': 'Retype password',
                                                                  'id': 'username'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')