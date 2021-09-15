from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from django.contrib.auth import authenticate
import requests

User = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'placeholder': 'Email Address', 'class': 'u-border-1 u-border-grey-75 u-custom-font u-font-roboto-condensed u-grey-5 u-input u-input-rectangle u-radius-10'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','class': 'u-border-1 u-border-grey-75 u-custom-font u-font-roboto-condensed u-grey-5 u-input u-input-rectangle u-radius-10'}))
    class Meta:
        model = User
        fields = ['email', 'password']
    def clean(self, *args, **kwargs):
        username = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if username and password:
            if not User.objects.filter(email=username).exists():
                self.add_error("email", "User does not exist")
            user = authenticate(username=username, password=password)

            if user is None:
                self.add_error("password", "Password is incorrect")
                # raise forms.ValidationError("User does not exist")
        return super(LoginForm, self).clean(*args, **kwargs)


class RegisterForm(forms.ModelForm):
    """
    The default 

    """

    password = forms.CharField(label="",widget=forms.PasswordInput(attrs={"placeholder":"Password"}))
    password_2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password"}))

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'license_state', 'license_number', 'job_class']
        labels = {'email':"", 'first_name':"", 'last_name':"", 'license_state':"", 'license_number':"", 'job_class':""}
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        placeholders = {'email':'Enter a valid email address', 'first_name':"First Name", 'last_name':"Last Name", 'license_state':"License State", 'license_number':"License Number", 'job_class':'Job Class', 'password':"Password", 'password_2': 'Confirm Password'}

        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = placeholders[field_name]
        self.fields['first_name'].widget.attrs['class'] = "u-border-1 u-border-grey-30 u-custom-font u-font-roboto-condensed u-input u-input-rectangle u-radius-10 u-white"
        self.fields['last_name'].widget.attrs['class'] = "u-border-1 u-border-grey-30 u-custom-font u-font-roboto-condensed u-input u-input-rectangle u-radius-10 u-white"
        self.fields['email'].widget.attrs['class'] = "u-border-1 u-border-grey-30 u-custom-font u-font-roboto-condensed u-input u-input-rectangle u-radius-10 u-white"
        self.fields['job_class'].widget.attrs['class'] = "u-border-1 u-border-grey-30 u-custom-font u-font-roboto-condensed u-input u-input-rectangle u-radius-10 u-white"
        self.fields['password'].widget.attrs['class'] = 'u-border-1 u-border-grey-30 u-custom-font u-font-roboto-condensed u-input u-input-rectangle u-radius-10 u-white'
        self.fields['password_2'].widget.attrs['class'] = 'u-border-1 u-border-grey-30 u-custom-font u-font-roboto-condensed u-input u-input-rectangle u-radius-10 u-white'
        self.fields['license_state'].widget.attrs['class'] = 'u-border-1 u-border-grey-30 u-custom-font u-font-roboto-condensed u-input u-input-rectangle u-radius-10 u-white'
        self.fields['license_number'].widget.attrs['class'] = 'u-border-1 u-border-grey-30 u-custom-font u-font-roboto-condensed u-input u-input-rectangle u-radius-10 u-white'

    def clean_email(self):
        '''
        Verify email is available.
        '''
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is taken")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

    def license_verification(self):
        cleaned_data = super().clean()
        license_number = cleaned_data.get("license_number")
        license_state = cleaned_data.get("license_state")

        #BASIC REQUIREMENTS LIKE LENGTH, ETC
        if len(license_number)<5 and license_state=="OK":
            self.add_error("license_number", "Invalid License Number")

        valid = bool(requests.get("https://www.verifier.com", headers={"Authorization":"randomkey"}, data={"license_number": license_number}))

        if not valid:
            self.add_error("Invalid! License verification failed!")
        elif valid is None:
            self.add_error("Unknown Error: License verification failed!")
        return cleaned_data    

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.active = True
        if commit:
            user.save()
        return user


class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """

    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'license_state', 'license_number']

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['email', 'password', 'active', 'admin', 'first_name', 'last_name', 'license_state', 'license_number']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]