from django import forms
# Create your forms here.
class Student_Registration(forms.Form):
    student_name = forms.CharField(max_length=15)
    father_name = forms.CharField(max_length=15, required=False)
    mother_name = forms.CharField(max_length=15, required=False)
    bangla = forms.IntegerField(max_value=100,min_value=1)
    english = forms.IntegerField(max_value=100,min_value=1)
    math = forms.IntegerField(max_value=100,min_value=1)
    social_science = forms.IntegerField(max_value=100,min_value=1)
    general_science = forms.IntegerField(max_value=100,min_value=1)
    religion = forms.IntegerField(max_value=100,min_value=1)
    point = forms.DecimalField(max_value=6 ,min_value=1, decimal_places=2)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(),error_messages={'required':'Enter Your Password'})
    confirm_password = forms.CharField( widget=forms.PasswordInput(),error_messages={'required':'Enter Your Password'})
    text_area = forms.CharField(widget=forms.Textarea(attrs={ 'rows':4, 'cols':40}))
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Password does not match")




