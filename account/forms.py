from django import forms
from .models import Student

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'form-control',
    }))
    
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'student_id',
            'department_name',
            'phone_number',
            'session'
        ]
        
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            raise forms.ValidationError(
                'Password does not match!'
            )
        def __init__(self, *args, **kwargs):
            super(RegistrationForm, self).__init__(*args, **kwargs)
            self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your first name'
            self.fields['last_name'].widget.attrs['placeholder'] = 'Enter your last name'
            self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
            self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
            self.fields['student_id'].widget.attrs['placeholder'] = 'Enter your student identifier'
            self.fields['department_name'].widget.attrs['placeholder'] = 'Enter your department name'
            self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter your phone number'
            self.fields['sessions'].widget.attrs['placeholder'] = 'Enter your sessions'
            
            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'