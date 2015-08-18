from django import forms
from upline.models import Member

class MemberRegisterForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Member
        fields = ('birthday','name','gender','phone')
